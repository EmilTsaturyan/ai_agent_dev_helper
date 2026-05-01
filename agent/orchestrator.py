from agent.planner import Planner
from agent.builder import Builder
from agent.tester import Tester
from agent.fixer import Fixer
from agent.reviewer import Reviewer
from agent.state import AgentState
from core.logging import get_logger


logger = get_logger(__name__)


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
        logger.info(f"Plan created: {plan}")

        # 2. Build
        build_response = self.builder.run(plan)
        logger.info(f"Build build_: {build_response}")

        # 3. Test
        test_response = self.tester.run(plan)
        logger.info(f"Test response: {test_response}")

        # 4. Run tests and get results
        for i in range(3):
            state.iteration = i

            result = self.run_tests()
            state.test_results = result
            logger.info(f"Test results: {result}")

            if "failed" not in result.lower():
                logger.info("All tests passed!")
                break

            # Fix
            fix_response = self.fixer.run(result)
            logger.info(f"Fix response: {fix_response}")
        
        # 5. Review
        review = self.reviewer.run(plan)
        state.review = review
        logger.info(f"Review response: {review}")

        return state
        