# 1. Use the updated, non-deprecated package import
from langchain_ollama import ChatOllama

# Simulated state dictionary for testing
state = {"model_name": "llama3.1:8b", "temperature": 0.2}

# 2. Initialize the model
llm = ChatOllama(
    model=state.get("model_name", "llama3.1:8b"), 
    temperature=state.get("temperature", 0.2)
)

# 3. Format the input strictly as a list of message dictionaries
messages = [
    {"role": "user", "content": "What is LangChain?"}
]

# 4. Invoke the model correctly
result = llm.invoke(messages)

# 5. Print the text content of the result (instead of the raw AI Message object)
print(result.content)
