import functools


def log_tool(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"\n🛠 TOOL CALL: {func.__name__}")
        print(f"ARGS: {args} {kwargs}")

        result = func(*args, **kwargs)

        print(f"RESULT: {result}\n")
        return result

    return wrapper