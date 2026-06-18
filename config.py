import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    
    # LangSmith Tracing Configuration
    LANGCHAIN_TRACING_V2 = os.getenv("LANGSMITH_TRACING")
    LANGCHAIN_ENDPOINT = os.getenv("LANGCHAIN_ENDPOINT")
    LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
    LANGCHAIN_PROJECT = os.getenv("LANGCHAIN_PROJECT")

    @classmethod
    def validate(cls):
        if not cls.OPENAI_API_KEY:
            raise ValueError("CRITICAL: OPENAI_API_KEY is missing from environment variables.")
        if cls.LANGCHAIN_TRACING_V2 == "true" and not cls.LANGCHAIN_API_KEY:
            print("WARNING: LangSmith tracing is enabled but LANGCHAIN_API_KEY is missing.")