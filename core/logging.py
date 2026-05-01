import functools
import logging
import os
from typing import Any


_MAX_LOG_VALUE_LENGTH = 300
_REDACT_KEYS = {"api_key", "apikey", "token", "secret", "password"}


def configure_logging() -> None:
    """Configure application logging once."""
    level_name = os.getenv("LOG_LEVEL", "INFO").upper()
    level = getattr(logging, level_name, logging.INFO)

    root_logger = logging.getLogger()
    if root_logger.handlers:
        root_logger.setLevel(level)
        return

    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
    )


def get_logger(name: str) -> logging.Logger:
    configure_logging()
    return logging.getLogger(name)


def _truncate(value: str) -> str:
    if len(value) <= _MAX_LOG_VALUE_LENGTH:
        return value
    return f"{value[:_MAX_LOG_VALUE_LENGTH]}... <truncated>"


def _sanitize(value: Any) -> Any:
    if isinstance(value, dict):
        sanitized = {}
        for key, item in value.items():
            if str(key).lower() in _REDACT_KEYS:
                sanitized[key] = "<redacted>"
            else:
                sanitized[key] = _sanitize(item)
        return sanitized

    if isinstance(value, (list, tuple)):
        return [_sanitize(item) for item in value]

    if isinstance(value, str):
        return _truncate(value)

    return value


def log_tool(func):
    logger = get_logger(f"tool.{func.__name__}")

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(
            "Tool call started",
            extra={
                "tool_name": func.__name__,
                "tool_args": _sanitize(args),
                "tool_kwargs": _sanitize(kwargs),
            },
        )
        try:
            result = func(*args, **kwargs)
        except Exception:
            logger.exception("Tool call failed", extra={"tool_name": func.__name__})
            raise

        logger.info(
            "Tool call completed",
            extra={
                "tool_name": func.__name__,
                "result": _sanitize(result),
            },
        )
        return result

    return wrapper