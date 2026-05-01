from agent.planner import Planner
from agent.builder import Builder
from agent.tester import Tester
from agent.fixer import Fixer
from agent.reviewer import Reviewer
from agent.state import AgentState


class Orchestrator:
    def __init__(self, llm, run_tests_tool):
        self.planner = Planner(llm)
        self.builder = Builder(llm)
        self.tester = Tester(llm)
        self.fixer = Fixer(llm)
        self.reviewer = Reviewer(llm)

        self.run_tests = run_tests_tool

    def run(self, task_description: str):
        state = AgentState(task=task_description)

        # 1. Plan
        plan = self.planner.run(task_description)
        state.plan = plan

        # 2. Build
        self.builder.run(plan)

        # 3. Test
        self.tester.run(plan)

        # 4. Run tests and get results
        for i in range(3):
            state.iteration = i

            result = self.run_tests()
            state.test_results = result

            if "failed" not in result.lower():
                break

            # Fix
            self.fixer.run(result)
        
        # 5. Review
        review = self.reviewer.run(plan)
        state.review = review

        return state
        