from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI

from prompts.system import SYSTEM_PROMPT
from tools.filesystem import read_file, write_file, list_files
from config.settings import settings


def build_agent():
    llm = create_agent(
            ChatGoogleGenerativeAI(model=settings.model),
            system_prompt=SYSTEM_PROMPT,
            tools=[read_file, write_file, list_files],
    )
    return llm