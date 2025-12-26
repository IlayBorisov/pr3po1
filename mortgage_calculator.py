class MortgageCalculator:
    def __init__(self, principal, annual_rate, years):
        """
        Инициализация калькулятора ипотеки

        Args:
            principal (float): Сумма кредита
            annual_rate (float): Годовая процентная ставка (%)
            years (int): Срок кредита в годах
        """
        self.principal = principal
        self.monthly_rate = annual_rate / 100 / 12
        self.months = years * 12

    def calculate_monthly_payment(self):
        """
        Рассчитать ежемесячный платеж

        Returns:
            float: Ежемесячный платеж
        """
        if self.monthly_rate == 0:
            return self.principal / self.months

        r = self.monthly_rate
        n = self.months

        monthly_payment = self.principal * (r * (1 + r) ** n) / ((1 + r) ** n - 1)
        return round(monthly_payment, 2)

    def calculate_total_payment(self):
        """
        Рассчитать общую сумму выплат

        Returns:
            float: Общая сумма выплат
        """
        monthly_payment = self.calculate_monthly_payment()
        return round(monthly_payment * self.months, 2)

    def calculate_overpayment(self):
        """
        Рассчитать переплату по кредиту

        Returns:
            float: Сумма переплаты
        """
        total_payment = self.calculate_total_payment()
        return round(total_payment - self.principal, 2)

    def calculate_payment_schedule(self):
        """
        Рассчитать график платежей

        Returns:
            list: Список словарей с данными по месяцам
        """
        schedule = []
        balance = self.principal
        monthly_payment = self.calculate_monthly_payment()

        for month in range(1, self.months):
            interest_payment = balance * self.monthly_rate
            principal_payment = monthly_payment - interest_payment
            balance -= principal_payment

            schedule.append({
                'month': month,
                'payment': monthly_payment,
                'principal': round(principal_payment, 2),
                'interest': round(interest_payment, 2),
                'balance': round(balance, 2)
            })

        # Последний месяц - особый случай
        last_interest = balance * self.monthly_rate
        last_payment = balance + last_interest
        schedule.append({
            'month': self.months,
            'payment': round(last_payment, 2),
            'principal': round(balance, 2),
            'interest': round(last_interest, 2),
            'balance': 0.0
        })

        return schedule


def main():
    """Основная функция для запуска калькулятора"""
    print("=== Калькулятор ипотеки ===")

    try:
        principal = float(input("Введите сумму кредита: "))
        annual_rate = float(input("Введите годовую процентную ставку (%): "))
        years = int(input("Введите срок кредита (лет): "))

        calculator = MortgageCalculator(principal, annual_rate, years)

        print("\nРезультаты расчета:")
        print(f"Ежемесячный платеж: {calculator.calculate_monthly_payment()} руб.")
        print(f"Общая сумма выплат: {calculator.calculate_total_payment()} руб.")
        print(f"Переплата по кредиту: {calculator.calculate_overpayment()} руб.")

        # Спросим, показать ли график платежей
        show_schedule = input("\nПоказать график платежей? (да/нет): ").lower()
        if show_schedule == 'да':
            schedule = calculator.calculate_payment_schedule()
            print("\nГрафик платежей (первые 12 месяцев):")
            print("Месяц | Платеж | Основной долг | Проценты | Остаток")
            print("-" * 50)
            for payment in schedule[:12]:
                print(f"{payment['month']:5} | {payment['payment']:7} | "
                      f"{payment['principal']:13} | {payment['interest']:8} | "
                      f"{payment['balance']:7}")

    except ValueError as e:
        print(f"Ошибка ввода данных: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
