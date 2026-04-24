from typing import List

from langchain.tools import tool

from config.settings import BASE_DIR
from core.logging import log_tool
from tools.utils import safe_path


@tool(description="Read a file and return its content")
@log_tool
def read_file(file_path: str) -> str:
    path = safe_path(file_path)    
    return path.read_text()


@tool(description="Create and/or overwrite a file with the given content")
@log_tool
def write_file(file_path: str, content: str) -> str:
    path = safe_path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)
    
    return f"File updated: {file_path}"


@tool(description="List all files in a working directory")
@log_tool
def list_files() -> List[str]:
    return [str(f.relative_to(BASE_DIR)) for f in BASE_DIR.rglob("*") if f.is_file()]


@tool(description="Create a new directory")
@log_tool
def create_directory(dir_path: str) -> str:
    path = safe_path(dir_path)
    path.mkdir(parents=True, exist_ok=True)
    return f"Directory created: {dir_path}"