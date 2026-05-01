from agent.base import BaseAgent


BUILDER_PROMPT = """
You are a backend developer.

Based on the plan:
- Create or modify files
- Use tools if available
- Follow FastAPI best practices
"""


class Builder(BaseAgent):
    def __init__(self, llm):
        super().__init__(llm, BUILDER_PROMPT)