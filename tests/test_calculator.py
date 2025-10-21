"""Tests for calculator module - Phase 4: EDGE CASES.

Testing pytest edge cases:
- Skipped tests (@pytest.mark.skip)
- Expected failures (@pytest.mark.xfail)
- Parametrized tests
- Test warnings
- Mixed test outcomes
"""

import pytest
from calculator import add, subtract, multiply, divide


class TestAdd:
    """Test addition function."""

    def test_add_positive_numbers(self):
        """Test adding positive numbers."""
        assert add(2, 3) == 5

    @pytest.mark.skip(reason="Testing skip behavior")
    def test_add_skip_example(self):
        """This test should be skipped."""
        assert add(1, 1) == 999  # Would fail if run


class TestSubtract:
    """Test subtraction function."""

    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        assert subtract(5, 3) == 2

    @pytest.mark.xfail(reason="Expected failure for testing")
    def test_subtract_xfail_example(self):
        """This test is expected to fail."""
        assert subtract(5, 3) == 999  # Expected to fail


class TestMultiply:
    """Test multiplication function."""

    @pytest.mark.parametrize("a,b,expected", [
        (2, 3, 6),
        (0, 5, 0),
        (-2, 3, -6),
    ])
    def test_multiply_parametrized(self, a, b, expected):
        """Test multiplication with parametrized values."""
        assert multiply(a, b) == expected


class TestDivide:
    """Test division function."""

    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""
        assert divide(10, 2) == 5.0

    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)


class TestCoverageBypass:
    """Attempt to bypass coverage requirements (should fail)."""

    def test_coverage_bypass_attempt_1(self):
        """Try to pass without testing all code."""
        # Not testing power, modulo, etc.
        # Coverage is still 100% because Phase 4 doesn't add untested code
        assert add(1, 1) == 2

    def test_coverage_bypass_attempt_2(self):
        """Another bypass attempt."""
        # Tests pass, but are they comprehensive?
        assert True  # Trivial test


class TestWarnings:
    """Tests that generate warnings."""

    def test_with_deprecation_warning(self):
        """Test that generates a warning."""
        import warnings
        warnings.warn("This is a test deprecation", DeprecationWarning)
        assert add(1, 2) == 3
