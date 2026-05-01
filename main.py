from core.logging import get_logger
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI

from tools.filesystem import read_file, write_file, list_files
from config.settings import settings
from agent.orchestrator import Orchestrator


def run_tests():
    import subprocess
    return subprocess.getoutput("pytest")


def main():
    logger = get_logger(__name__)

    agent = create_agent(
        ChatGoogleGenerativeAI(model=settings.model),
        tools=[read_file, write_file, list_files],
    )

    orchestrator = Orchestrator(agent, list_files)
    prompt = "Create a new fastapi project with a single endpoint that returns Hello World, use layered architecture with DI module, and write tests for it."

    try:
        orchestrator.run(prompt)
    except Exception as e:
        logger.error(f"Error during execution: {e}")
    

if __name__ == "__main__":
    main()