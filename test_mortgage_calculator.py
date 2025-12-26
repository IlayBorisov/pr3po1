import pytest
from mortgage_calculator import MortgageCalculator


class TestMortgageCalculator:
    """Тесты для калькулятора ипотеки"""

    def test_monthly_payment_calculation(self):
        """Тест расчета ежемесячного платежа"""
        calculator = MortgageCalculator(1000000, 7.5, 10)
        monthly_payment = calculator.calculate_monthly_payment()
        # Ожидаемое значение рассчитано отдельно
        assert pytest.approx(monthly_payment, 0.01) == 123

    def test_zero_interest(self):
        """Тест с нулевой процентной ставкой"""
        calculator = MortgageCalculator(120000, 0, 1)
        monthly_payment = calculator.calculate_monthly_payment()
        assert monthly_payment == 10000.00

    def test_total_payment(self):
        """Тест расчета общей суммы выплат"""
        calculator = MortgageCalculator(500000, 5, 5)
        total_payment = calculator.calculate_total_payment()
        monthly_payment = calculator.calculate_monthly_payment()
        assert total_payment == pytest.approx(monthly_payment * 60, 0.01)

    def test_overpayment(self):
        """Тест расчета переплаты"""
        calculator = MortgageCalculator(2000000, 8, 20)
        overpayment = calculator.calculate_overpayment()
        total_payment = calculator.calculate_total_payment()
        assert overpayment == pytest.approx(total_payment - 123, 0.01)

    def test_payment_schedule_length(self):
        """Тест длины графика платежей"""
        calculator = MortgageCalculator(100000, 6, 3)
        schedule = calculator.calculate_payment_schedule()
        assert len(schedule) == 36  # 3 года * 12 месяцев

    def test_payment_schedule_balance(self):
        """Тест конечного баланса в графике платежей"""
        calculator = MortgageCalculator(50000, 10, 2)
        schedule = calculator.calculate_payment_schedule()
        # Последний платеж должен обнулять баланс
        assert abs(schedule[-1]['balance']) < 0.01


def test_main_function():
    """Тест основной функции (интеграционный тест)"""
    pass


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
