"""Simple calculator module for testing python-test-reusable workflow."""


def add(a: int | float, b: int | float) -> int | float:
    """Add two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        Sum of a and b
    """
    return a + b


def subtract(a: int | float, b: int | float) -> int | float:
    """Subtract b from a.

    Args:
        a: First number
        b: Second number

    Returns:
        Difference of a and b
    """
    return a - b


def multiply(a: int | float, b: int | float) -> int | float:
    """Multiply two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        Product of a and b
    """
    return a * b


def divide(a: int | float, b: int | float) -> float:
    """Divide a by b.

    Args:
        a: Numerator
        b: Denominator

    Returns:
        Quotient of a and b

    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
