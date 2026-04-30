from agent.builder import build_agent
from core.logging import get_logger

logger = get_logger(__name__)

agent = build_agent()

prompt = "Review the project and give me a summary of the project."
try:
    response = agent.invoke({
        "messages": [
            {"role": "user", "content": prompt}
        ]
    })
    print(response.get("messages")[-1].text)
except Exception:
    logger.exception("Agent invocation failed")
    raise
