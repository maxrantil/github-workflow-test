"""Tests for calculator module - Phase 2: FAILING TESTS."""

import pytest
from calculator import add, subtract, multiply, divide


class TestAdd:
    """Test addition function - with assertion failures."""

    def test_add_positive_numbers_FAIL(self):
        """Test adding positive numbers - WRONG expected value."""
        assert add(2, 3) == 6  # FAIL: Should be 5

    def test_add_negative_numbers_FAIL(self):
        """Test adding negative numbers - WRONG expected value."""
        assert add(-2, -3) == -4  # FAIL: Should be -5


class TestSubtract:
    """Test subtraction function - with assertion failures."""

    def test_subtract_positive_numbers_FAIL(self):
        """Test subtracting positive numbers - WRONG expected value."""
        assert subtract(5, 3) == 3  # FAIL: Should be 2

    def test_subtract_logic_error_FAIL(self):
        """Test subtraction - backwards logic."""
        assert subtract(10, 3) == 3  # FAIL: Should be 7


class TestMultiply:
    """Test multiplication function - with exceptions."""

    def test_multiply_raises_unexpected_exception_FAIL(self):
        """Test that should raise ValueError but doesn't."""
        with pytest.raises(ValueError):  # FAIL: multiply doesn't raise
            multiply(3, 4)

    def test_multiply_wrong_exception_type_FAIL(self):
        """Test expecting wrong exception type."""
        with pytest.raises(TypeError):  # FAIL: divide raises ValueError
            divide(10, 0)


class TestDivide:
    """Test division function - with assertion failures."""

    def test_divide_positive_numbers_FAIL(self):
        """Test dividing positive numbers - WRONG expected value."""
        assert divide(10, 2) == 4.0  # FAIL: Should be 5.0

    def test_divide_missing_exception_check_FAIL(self):
        """Test divide by zero without catching exception."""
        # FAIL: This will raise ValueError but we don't catch it
        result = divide(10, 0)
        assert result == 0


class TestSyntaxErrors:
    """Tests with syntax errors - should fail during collection."""

    def test_syntax_error_FAIL(self):
        """Test with intentional syntax error."""
        # FAIL: Syntax error - missing closing parenthesis
        assert add(2, 3 == 5


class TestImportErrors:
    """Tests with import errors."""

    def test_import_nonexistent_module_FAIL(self):
        """Test importing non-existent module."""
        # FAIL: Module doesn't exist
        from nonexistent_module import fake_function
        assert fake_function() == True
