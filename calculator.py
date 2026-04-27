def calculate_simple_interest(principal: float, rate: float, time: float) -> float:
    """Расчёт простых процентов."""
    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("Аргументы должны быть неотрицательными")
    return float(principal * rate * time / 100)


def calculate_compound_interest(principal: float, rate: float, time: float, n: int = 1) -> float:
    """Расчёт сложных процентов."""
    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("Аргументы должны быть неотрицательными")
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Параметр n должен быть целым положительным числом")
    
    return float(principal * (1 + rate / (100 * n)) ** (n * time))


def calculate_tax(amount: float, tax_rate: float) -> float:
    """Расчёт суммы налога."""
    if not (0 <= tax_rate <= 100):
        raise ValueError("Ставка налога должна быть в диапазоне от 0 до 100")
    return float(amount * tax_rate / 100)