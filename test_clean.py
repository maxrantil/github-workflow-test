"""Clean Python file for Phase 1 testing - should pass all pre-commit hooks."""


def hello_world():
    """Return a greeting message."""
    return "Hello, World!"


def add_numbers(a, b):
    """Add two numbers together."""
    return a + b


if __name__ == "__main__":
    print(hello_world())
    print(f"2 + 3 = {add_numbers(2, 3)}")
