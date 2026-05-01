from agent.base import BaseAgent


TESTER_PROMPT = """
You are a QA engineer.

Write pytest tests for the project.
Focus on:
- edge cases
- API responses
"""


class Tester(BaseAgent):
    def __init__(self, llm):
        super().__init__(llm, TESTER_PROMPT)