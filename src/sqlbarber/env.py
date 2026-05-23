import os
from pathlib import Path


def load_dotenv(path=None, override=False):
    """Load simple KEY=VALUE pairs from a .env file into os.environ."""
    env_path = Path(path) if path else Path(__file__).resolve().parents[2] / ".env"
    if not env_path.exists():
        return False

    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()

        if not key:
            continue

        if value and value[0] == value[-1] and value[0] in ("'", '"'):
            value = value[1:-1]

        if override or key not in os.environ:
            os.environ[key] = value

    return True


def get_llm_config():
    api_key = (
        os.getenv("LLM_API_KEY")
        or os.getenv("OPENAI_API_KEY")
        or os.getenv("DEEPSEEK_API_KEY")
    )
    api_base = (
        os.getenv("LLM_BASE_URL")
        or os.getenv("LLM_API_BASE")
        or os.getenv("OPENAI_BASE_URL")
        or os.getenv("DEEPSEEK_BASE_URL")
    )
    model = os.getenv("LLM_MODEL", "o3-mini")

    return api_key, api_base, model
