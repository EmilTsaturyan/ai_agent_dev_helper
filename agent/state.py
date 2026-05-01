from dataclasses import dataclass


@dataclass
class AgentState:
    task: str
    plan: str = ""
    test_results: str = ""
    review: str = ""
    iteration: int = 0