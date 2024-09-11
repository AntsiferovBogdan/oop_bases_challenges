"""
У любого продукта есть такие свойства: название, описание, цена, вес

Задания:
    1. Создайте класс продукта.
    2. Создайте экземпляр этого продукта и наполинте своими данными.
    3. Распечатайте о нем иформацию в таком виде: Информация о продукте: название, описание, цена, вес
"""
# from dataclasses import dataclass


# 1. Стандартное описание класса
class Product:
    def __init__(self, name: str, description: str, price: int, weight: int):
        self.name = name
        self.description = description
        self.price = price
        self.weight = weight

# 2. С использованием декоратора
# @dataclass
# class Product:
#     name: str
#     description: str
#     price: int
#     weight: int


if __name__ == '__main__':
    new_product = Product(
        'iPhone 16',
        'Amazing and powerful',
        799,
        170,
        )
    print(f'Информация о продукте: {new_product.name}, {new_product.description}, {new_product.price}, {new_product.weight}')
