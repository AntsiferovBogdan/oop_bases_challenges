"""
У нас есть различные типы классы для различных типов продуктов. Но мы ничего не знаем о том что происходит, когда мы вызываем
эти методы, хотелось бы простейшего логирования

Задания:
    1. Создайте класс PrintLoggerMixin и метод log у него, который будет принтить переданное в него сообщение.
    2. Используйте этот миксин, чтобы залогировать все методы у PremiumProduct и DiscountedProduct.
       Добавьте миксин и используйте новый метод во всех методах основных классов.
    3. Вызовите у экземпляров PremiumProduct и DiscountedProduct все возможные методы и убедитесь, что вызовы логируются.
"""
from datetime import datetime
from inspect import currentframe


class PrintLoggerMixin:
    def log(self, message: str) -> None:
        now = datetime.now().strftime('%d %B %Y %H:%M:%S')
        print(f'{now}. Called {message}')


class Product:
    def __init__(self, title: str, price: float):
        self.title = title
        self.price = price

    def get_info(self):
        return f'Product {self.title} with price {self.price}'


class PremiumProduct(PrintLoggerMixin, Product):
    def increase_price(self):
        self.log(f'{self.__class__.__name__}.{currentframe().f_code.co_name}')
        self.price *= 1.2

    def get_info(self) -> str:
        self.log(f'{self.__class__.__name__}.{currentframe().f_code.co_name}')
        base_info = super().get_info()
        return f'{base_info} (Premium)'


class DiscountedProduct(PrintLoggerMixin, Product):
    def decrease_price(self) -> None:
        self.log(f'{self.__class__.__name__}.{currentframe().f_code.co_name}')
        self.price /= 1.2

    def get_info(self) -> str:
        self.log(f'{self.__class__.__name__}.{currentframe().f_code.co_name}')
        base_info = super().get_info()
        return f'{base_info} (Discounted)'


if __name__ == '__main__':
    iphone = PremiumProduct('iPhone 16', 799.0)
    iphone.increase_price()
    print(iphone.get_info())

    milk = DiscountedProduct('Milk', 9.99)
    milk.decrease_price()
    print(milk.get_info())
