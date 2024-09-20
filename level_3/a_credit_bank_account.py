"""
У нас есть класс кредитного банковского аккаунта со свойствами: полное имя владельца и баланс.

Задания:
    1. Нужно вынести методы, которые не относится непосредственно к кредитам в отдельны класс BankAccount.
    2. CreditAccount нужно отнаследовать от BankAccount.
    3. Создать экземпляр класс BankAccount и вызвать у него каждый из возможных методов.
    4. Создать экземпляр класс CreditAccount и вызвать у него каждый из возможных методов.
"""
from dataclasses import dataclass


@dataclass(kw_only=True, slots=True)
class BankAccount:
    owner_full_name: str
    balance: float

    def increase_balance(self, amount: float) -> None:
        self.balance += amount

    def decrease_balance(self, amount: float) -> None:
        self.balance -= amount


@dataclass()
class CreditAccount(BankAccount):

    def is_eligible_for_credit(self) -> bool:
        return self.balance > 1000


if __name__ == '__main__':
    new_bank_account = BankAccount(
        owner_full_name='Elon Musk',
        balance=500,
    )
    new_bank_account.increase_balance(100)
    new_bank_account.decrease_balance(300)
    print(new_bank_account)

    new_credit_account = CreditAccount(
        owner_full_name='Pavel Durov',
        balance=0
    )
    print(new_credit_account.is_eligible_for_credit())
    new_credit_account.increase_balance(3000)
    new_credit_account.decrease_balance(1000)
    print(new_credit_account.is_eligible_for_credit())
