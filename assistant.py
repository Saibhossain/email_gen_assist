from typing import TypedDict, Optional
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langgraph.graph import StateGraph, START, END
from prompts import EMAIL_GENERATION_SYSTEM_PROMPT

# Define State Structure
class AssistantState(TypedDict):
    intent: str
    key_facts: str
    tone: str
    model_name: str
    temperature: float
    raw_output: Optional[str]
    thinking_process: Optional[str]
    clean_email: Optional[str]

def generate_email_node(state: AssistantState) -> dict:
    """ LangGraph Node running our advanced generation prompt template """
    llm = ChatOpenAI(
        model=state.get("model_name", "gpt-4o-mini"), 
        temperature=state.get("temperature", 0.2)
    )
    
    prompt_template = PromptTemplate.from_template(EMAIL_GENERATION_SYSTEM_PROMPT)
    formatted_prompt = prompt_template.format(
        intent=state["intent"],
        key_facts=state["key_facts"],
        tone=state["tone"]
    )
    
    response = llm.invoke(formatted_prompt)
    content = response.content
    
    # Process and strip out thinking tags if present for downstream extraction
    thinking = ""
    clean_text = content
    if "<thinking>" in content and "</thinking>" in content:
        parts = content.split("</thinking>")
        thinking = parts[0].replace("<thinking>", "").strip()
        clean_text = parts[1].strip()
        
    return {
        "raw_output": content, 
        "thinking_process": thinking, 
        "clean_email": clean_text
    }

# Build workflow Graph
workflow = StateGraph(AssistantState)
workflow.add_node("generation_agent", generate_email_node)
workflow.add_edge(START, "generation_agent")
workflow.add_edge("generation_agent", END)

# Compile Application
email_assistant_app = workflow.compile()

# Save the workflow graph as a PNG file
try:
    with open("workflow_graph.png", "wb") as f:
        f.write(email_assistant_app.get_graph().draw_mermaid_png())
    print("Graph saved successfully as 'workflow_graph.png'")
except Exception as e:
    print(class_name := type(e).__name__, f": {e}")