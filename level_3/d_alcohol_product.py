"""
У нас есть класс Product, который содержит в себе информацию о продукте.
Еще у нас есть класс AlcoholProduct, но метод is_available для него не подходит, так как
алкоголь нельзя продавать с 5 утра до 11 вечера

Задания:
    1. Переопределите метод is_available в классе AlcoholProduct с использованием super()
    2. is_available у AlcoholProduct должен возвращать False если сейчас часы между 5 утра и 11 вечера.
       Для определения текущего часа можно использовать datetime.now().hour
    3. Создайте экземпляр класса AlcoholProduct и проверьте, можно ли сейчас продавать алкоголь.
"""
from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, kw_only=True, slots=True)
class Product:
    title: str
    price: float
    stock_quantity: int

    def get_discounted_price(self, discount_percentage: float) -> float:
        return self.price * (1 - discount_percentage / 100)

    def is_available(self) -> bool:
        return self.stock_quantity > 0


@dataclass(frozen=True)
class AlcoholProduct(Product):

    def is_available(self) -> bool:
        return self.stock_quantity > 0 and not (datetime.now().hour in range(5, 23))


if __name__ == '__main__':
    tequila = AlcoholProduct(
        title='olmeca gold',
        price=19.85,
        stock_quantity=100,
    )
    print(tequila.is_available())
