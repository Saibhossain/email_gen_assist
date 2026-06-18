import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    
    # LangSmith Tracing Configuration
    LANGSMITH_TRACING = os.getenv("LANGSMITH_TRACING","true")
    LANGCHAIN_ENDPOINT = os.getenv("LANGCHAIN_ENDPOINT", "https://api.smith.langchain.com")
    LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")
    LANGCHAIN_PROJECT = os.getenv("LANGCHAIN_PROJECT","Email_assist")

    @classmethod
    def validate(cls):
        if not cls.OPENAI_API_KEY:
            raise ValueError("CRITICAL: OPENAI_API_KEY is missing from environment variables.")
        if cls.LANGSMITH_TRACING == "true" and not cls.LANGSMITH_API_KEY:
            print("WARNING: LangSmith tracing is enabled but LANGCHAIN_API_KEY is missing.")