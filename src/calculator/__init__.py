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


# UNTESTED FUNCTIONS - Will reduce coverage below 80%
def power(base: int | float, exponent: int | float) -> int | float:
    """Raise base to the power of exponent.

    Args:
        base: The base number
        exponent: The exponent

    Returns:
        base raised to exponent
    """
    return base ** exponent


def modulo(a: int, b: int) -> int:
    """Calculate modulo (remainder of division).

    Args:
        a: Dividend
        b: Divisor

    Returns:
        Remainder of a divided by b

    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a % b


def square_root(n: float) -> float:
    """Calculate square root.

    Args:
        n: Number to find square root of

    Returns:
        Square root of n

    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return n ** 0.5


def absolute(n: int | float) -> int | float:
    """Calculate absolute value.

    Args:
        n: Number to find absolute value of

    Returns:
        Absolute value of n
    """
    return abs(n)


def factorial(n: int) -> int:
    """Calculate factorial.

    Args:
        n: Non-negative integer

    Returns:
        Factorial of n

    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
