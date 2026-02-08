from pydantic_settings import BaseSettings
from typing import List, Optional
import json

class Settings(BaseSettings):
    # App info
    APP_NAME: str
    APP_VERSION: str

    # API Keys
    OPENAI_API_KEY: Optional[str]
    OPENAI_API_URL: Optional[str]
    COHERE_API_KEY: Optional[str]

    # File handling
    FILE_ALLOWED_TYPES: List[str]
    FILE_MAX_SIZE: int
    FILE_DEFAULT_CHUNK_SIZE: int

    # Postgres
    POSTGRES_USERNAME: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_MAIN_DATABASE: str

    # Generation / Embeddings
    GENERATION_BACKEND: str
    EMBEDDING_BACKEND: str
    GENERATION_MODEL_ID_LITERAL: List[str]
    GENERATION_MODEL_ID: str
    EMBEDDING_MODEL_ID: str
    EMBEDDING_MODEL_SIZE: int

    # Generation defaults
    INPUT_DEFAULT_MAX_CHARACTERS: int
    GENERATION_DEFAULT_MAX_OUTPUT_TOKENS: int
    GENERATION_DEFAULT_TEMPERATURE: float

    # Vector DB
    VECTOR_DB_BACKEND_LITERAL: List[str]
    VECTOR_DB_BACKEND: str
    VECTOR_DB_PATH: str
    VECTOR_DB_DISTANCE_METHOD: str
    VECTOR_DB_PGVEC_INDEX_THRESHOLD: int

    # Language
    PRIMARY_LANG: str
    DEFAULT_LANG: str

    class Config:
        env_file = ".env"
        extra = "forbid"
        @staticmethod
        def parse_env_var(field, raw_val):
            if field.type_ == List[str]:
                return json.loads(raw_val)
            return raw_val

def get_settings() -> Settings:
    return Settings()
