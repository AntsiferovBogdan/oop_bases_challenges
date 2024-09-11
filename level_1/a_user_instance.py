"""
Задания:
    1. Создайте экземпляр класса юзера, наполнив любыми данными.
    2. Распечатайте информацию о нем в таком виде: Информация о пользователе: имя, юзернэйм, возраст, телефон.
"""


class User:
    def __init__(self, name: str, username: str, age: int, phone: str):
        self.name = name
        self.username = username
        self.age = age
        self.phone = phone


if __name__ == '__main__':
    new_user = User(
        'sasha',
        'alexdarkstalker98',
        12,
        '79121234567',
    )
    print(f'Информация о пользователе: {new_user.name}, {new_user.username}, {new_user.age}, {new_user.phone}')
