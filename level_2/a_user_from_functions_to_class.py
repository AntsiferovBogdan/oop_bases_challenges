""""
У нас есть функции для работы с пользователем, но хочется работать с ним через класс.

Задания:
    1. Создайте класс User и перенесите всю логику работы с пользователем туда.
"""
from dataclasses import dataclass


@dataclass(frozen=True, kw_only=True, slots=True)
class User:
    username: str
    user_id: int
    name: str

    def make_username_capitalized(self) -> str:
        return self.username.capitalize()

    def generate_short_user_description(self) -> str:
        return f'User with id {self.user_id} has {self.username} username and {self.name} name'


if __name__ == '__main__':
    new_user = User(
        username='admin',
        user_id=1,
        name='vasya',
    )
    print(new_user.make_username_capitalized())
    print(new_user.generate_short_user_description())
