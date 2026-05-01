from agent.base import BaseAgent


REVIEWER_PROMPT = """
You are a code reviewer.

Evaluate:
- code quality
- structure
- best practices

Return score from 1 to 10 and suggestions.
"""


class Reviewer(BaseAgent):
    def __init__(self, llm):
        super().__init__(llm, REVIEWER_PROMPT)