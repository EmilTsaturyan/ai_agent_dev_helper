from pathlib import Path
from config.settings import BASE_DIR


def safe_path(path: str) -> Path:
    full_path = (BASE_DIR / path).resolve()

    if not str(full_path).startswith(str(BASE_DIR)):
        raise ValueError(f"Access denied: {path}")

    return full_path