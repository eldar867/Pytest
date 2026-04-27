import pytest
from calculator import calculate_simple_interest, calculate_compound_interest, calculate_tax


# ==================== Simple Interest ====================
class TestCalculateSimpleInterest:
    def test_basic_calculations(self):
        assert calculate_simple_interest(1000, 5, 2) == 100.0
        assert calculate_simple_interest(500, 10, 3) == 150.0

    def test_zero_values(self):
        assert calculate_simple_interest(0, 5, 2) == 0.0
        assert calculate_simple_interest(1000, 0, 2) == 0.0
        assert calculate_simple_interest(1000, 5, 0) == 0.0

    def test_negative_values(self):
        with pytest.raises(ValueError, match="Аргументы должны быть неотрицательными"):
            calculate_simple_interest(-100, 5, 2)
        with pytest.raises(ValueError, match="Аргументы должны быть неотрицательными"):
            calculate_simple_interest(100, -5, 2)


# ==================== Compound Interest ====================
class TestCalculateCompoundInterest:
    def test_basic_calculations(self):
        assert calculate_compound_interest(1000, 5, 2) == 1102.5
        assert calculate_compound_interest(1000, 5, 2, n=4) == pytest.approx(1104.486101181412)

    def test_zero_values(self):
        assert calculate_compound_interest(0, 5, 2) == 0.0
        assert calculate_compound_interest(1000, 0, 2) == 1000.0
        assert calculate_compound_interest(1000, 5, 0) == 1000.0

    def test_invalid_arguments(self):
        with pytest.raises(ValueError):
            calculate_compound_interest(-100, 5, 2)
        with pytest.raises(ValueError):
            calculate_compound_interest(100, 5, 2, n=-1)
        with pytest.raises(ValueError):
            calculate_compound_interest(100, 5, 2, n=1.5)  # не целое
        with pytest.raises(ValueError):
            calculate_compound_interest(100, 5, 2, n=0)    # не положительное


# ==================== Tax ====================
class TestCalculateTax:
    def test_basic_calculations(self):
        assert calculate_tax(1000, 20) == 200.0
        assert calculate_tax(2500, 13) == 325.0

    def test_zero_values(self):
        assert calculate_tax(0, 20) == 0.0
        assert calculate_tax(1000, 0) == 0.0

    def test_invalid_tax_rate(self):
        with pytest.raises(ValueError):
            calculate_tax(1000, -5)
        with pytest.raises(ValueError):
            calculate_tax(1000, 105)