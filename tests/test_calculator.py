"""Tests for calculator module - 100% coverage."""

import pytest
from calculator import add, subtract, multiply, divide


class TestAdd:
    """Test addition function."""

    def test_add_positive_numbers(self):
        """Test adding positive numbers."""
        assert add(2, 3) == 5

    def test_add_negative_numbers(self):
        """Test adding negative numbers."""
        assert add(-2, -3) == -5

    def test_add_mixed_numbers(self):
        """Test adding positive and negative numbers."""
        assert add(5, -3) == 2

    def test_add_zero(self):
        """Test adding zero."""
        assert add(5, 0) == 5

    def test_add_floats(self):
        """Test adding floats."""
        assert add(2.5, 3.5) == 6.0


class TestSubtract:
    """Test subtraction function."""

    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        assert subtract(5, 3) == 2

    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers."""
        assert subtract(-5, -3) == -2

    def test_subtract_mixed_numbers(self):
        """Test subtracting mixed numbers."""
        assert subtract(5, -3) == 8

    def test_subtract_zero(self):
        """Test subtracting zero."""
        assert subtract(5, 0) == 5

    def test_subtract_floats(self):
        """Test subtracting floats."""
        assert subtract(5.5, 2.5) == 3.0


class TestMultiply:
    """Test multiplication function."""

    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        assert multiply(3, 4) == 12

    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers."""
        assert multiply(-3, -4) == 12

    def test_multiply_mixed_numbers(self):
        """Test multiplying mixed numbers."""
        assert multiply(3, -4) == -12

    def test_multiply_zero(self):
        """Test multiplying by zero."""
        assert multiply(5, 0) == 0

    def test_multiply_floats(self):
        """Test multiplying floats."""
        assert multiply(2.5, 4.0) == 10.0


class TestDivide:
    """Test division function."""

    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""
        assert divide(10, 2) == 5.0

    def test_divide_negative_numbers(self):
        """Test dividing negative numbers."""
        assert divide(-10, -2) == 5.0

    def test_divide_mixed_numbers(self):
        """Test dividing mixed numbers."""
        assert divide(10, -2) == -5.0

    def test_divide_floats(self):
        """Test dividing floats."""
        assert divide(7.5, 2.5) == 3.0

    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)
