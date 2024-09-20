"""
У нас есть класс UserManager, который содержит в себе спискок юзернэймов пользователей и может расширять этот список.

Задания:
    1. Создайте класс AdminManager, который будет наследником UserManager.
       У него должен быть свой уникальный метод ban_username, который по переданному в него юзернэйму будет удалять
       юзернэйм из списка. Если такого юзернэйма в списке нет - должно печататься сообщение: "Такого пользователя не существует."
    2. Создайте класс SuperAdminManager, который будет наследником AdminManager.
       У него должен быть свой уникальный метод ban_all_users, который будет удалять все юзернэймы из списка.
    3. Создайте экземпляры каждого из трех классов и у каждого экземпляра вызовите все возможные методы.
"""


class UserManager:
    def __init__(self, usernames: list[str]):
        self.usernames = usernames

    def add_user(self, username: str) -> None:
        self.usernames.append(username)

    def get_users(self) -> list[str]:
        return self.usernames


class AdminManager(UserManager):
    def ban_username(self, username: str) -> None:
        if username in self.usernames:
            self.usernames.remove(username)
        else:
            print('Такого пользователя не существует.')


class SuperAdminManager(AdminManager):
    def ban_all_users(self) -> None:
        self.usernames.clear()


if __name__ == '__main__':
    new_manager = UserManager(usernames=['mr. manager'])
    new_manager.add_user('good boy')
    new_manager.add_user('bad guy')
    print(new_manager.get_users())

    new_admin = AdminManager(usernames=['mr. admin'])
    new_admin.add_user('good boy')
    new_admin.add_user('bad guy')
    print(new_admin.get_users())
    new_admin.ban_username('mr. manager')
    new_admin.ban_username('good boy')
    print(new_admin.get_users())

    new_super_admin = SuperAdminManager(usernames=['mr. super_admin'])
    new_super_admin.add_user('good boy')
    new_super_admin.add_user('bad guy')
    print(new_super_admin.get_users())
    new_super_admin.ban_username('mr. manager')
    new_super_admin.ban_username('good boy')
    print(new_super_admin.get_users())
    new_super_admin.ban_all_users()
    print(new_super_admin.get_users())
