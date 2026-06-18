from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

import os
from dotenv import load_dotenv

load_dotenv()

state = {"model_name": "gpt-4.1-nano-2025-04-14", "temperature": 0.2}

llm = ChatOpenAI(
    model=state.get("model_name", "gpt-4.1-nano-2025-04-14"), 
    temperature=state.get("temperature", 0.2)
)

messages = [
    {"role": "user", "content": "What is LangChain?"}
]

result = llm.invoke(messages)

print(result.content)
