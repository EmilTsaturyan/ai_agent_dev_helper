from agent.base import BaseAgent


PLANNER_PROMPT = """
You are a senior engineer.

Create a step-by-step plan:
- What files to create
- What logic to implement
- What tests to write
"""


class Planner(BaseAgent):
    def __init__(self, llm):
        super().__init__(llm, PLANNER_PROMPT)