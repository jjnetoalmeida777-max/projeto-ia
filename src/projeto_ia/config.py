import os

from dotenv import load_dotenv

load_dotenv()


def get_env(name: str, required: bool = False) -> str | None:
    value = os.getenv(name)

    if required and not value:
        raise RuntimeError(f"Variavel de ambiente obrigatoria nao definida: {name}")

    return value


OPENAI_API_KEY = get_env("OPENAI_API_KEY")
GEMINI_API_KEY = get_env("GEMINI_API_KEY")
ANTHROPIC_API_KEY = get_env("ANTHROPIC_API_KEY")
