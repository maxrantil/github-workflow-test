"""Tests for calculator module - Phase 3: LOW COVERAGE.

Only tests 4 out of 9 functions, resulting in ~44% coverage (below 80% threshold).
"""

import pytest
from calculator import add, subtract, multiply, divide


class TestAdd:
    """Test addition function."""

    def test_add_positive_numbers(self):
        """Test adding positive numbers."""
        assert add(2, 3) == 5

    def test_add_zero(self):
        """Test adding zero."""
        assert add(5, 0) == 5


class TestSubtract:
    """Test subtraction function."""

    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        assert subtract(5, 3) == 2


class TestMultiply:
    """Test multiplication function."""

    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        assert multiply(3, 4) == 12


class TestDivide:
    """Test division function."""

    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""
        assert divide(10, 2) == 5.0

    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)


# NOT TESTING: power, modulo, square_root, absolute, factorial
# This creates ~44% coverage (10 statements out of ~68 total)
# Coverage requirement is 80%, so this should FAIL
