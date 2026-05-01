from agent.base import BaseAgent


FIXER_PROMPT = """
You are a senior developer fixing bugs.

Given test failures:
- identify root cause
- fix code
- do NOT break existing logic
"""


class Fixer(BaseAgent):
    def __init__(self, llm):
        super().__init__(llm, FIXER_PROMPT)