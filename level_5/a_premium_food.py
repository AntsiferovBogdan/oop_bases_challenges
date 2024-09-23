"""
У нас есть базовый класс продукта, а так же есть миксин для продуктов питания, но нет класса для продуктов питания.

Задания:
    1. Нужно создать класс FoodProduct, который будет наследовать от классов Product и FoodProductMixin.
    2. У класса FoodProduct переопределить метод get_product_info, таким образом,
        чтобы если продукт премиальный, то в скобках в конце добавлялось слово Premium.
        Например: Product title: Avocado, price: 12 (Premium)'
    3. Создать экземпляр класс FoodProduct с ценой меньше 10 и вызвать у него метод get_product_info.
    4. Создать экземпляр класс FoodProduct с ценой больше 10 и вызвать у него метод get_product_info.
"""


class Product:
    def __init__(self, title: str, price: float):
        self.title = title
        self.price = price

    def get_product_info(self) -> str:
        return f'Product title: {self.title}, price: {self.price}'


class FoodProductMixin:
    def is_premium_food(self) -> bool:
        return self.price > 10


class FoodProduct(Product, FoodProductMixin):
    def __init__(self, title: str, price: float):
        super().__init__(title, price)

    def get_product_info(self) -> str:
        product_info = super().get_product_info()
        if super().is_premium_food():
            product_info = f'{product_info} (Premium)'
        return product_info


if __name__ == '__main__':
    banana = FoodProduct('banana', 5)
    print(banana.get_product_info())

    fish = FoodProduct('fish', 15)
    print(fish.get_product_info())
