"""
Мы научились увеличивать баланс у банковского аккаунта, но иногда нам нужно и уменьшать его.

Задания:
    1. Возьмите итоговый класс из прошлого примера и добавьте ему метод, который уменьшает баланс.
       Если итоговое значение будет отрицательным, то нужно будет вызывать исключение ValueError.
    2. Создайте экземпляр класса и уменьшите баланс до положительного значения и распечатайте результат.
    3. Затем уменьшите баланс до отрицательного значения и посмотрите на результат
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, income: float):
        if income > 0:
            self.balance += income
        else:
            raise ValueError('Incorrect income value')

    def decrease_balance(self, outcome: float):
        if isinstance(outcome, (float, int)) and outcome <= self.balance:
            self.balance -= outcome
        else:
            raise ValueError('Insufficient funds on balance')


if __name__ == '__main__':
    account = BankAccount(
        'John Doe',
        100.0,
    )
    account.decrease_balance(20.0)
    print(account.balance)
    account.decrease_balance(100.0)
