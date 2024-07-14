"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product
from homework.models import Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(100) is True
        assert product.check_quantity(1000) is True
        assert product.check_quantity(1001) is False

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(990)
        assert product.quantity == 10
        assert product.buy(10) is None

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(2000)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, cart, product):
        cart.add_product(product, 2)
        assert cart.products[product] == 2

    def test_remove_products(self, cart, product):
        cart.add_product(product, 10)
        cart.remove_product(product, 5)
        assert cart.products[product] == 5
        print(cart.products[product])

    def test_remove_more_product_than_in_cart(self, cart, product):
        cart.add_product(product, 10)
        cart.remove_product(product, 20)
        assert product not in cart.products

    def test_remove_product_entirely(self, cart, product):
        cart.add_product(product, 20)
        cart.remove_product(product)
        assert product not in cart.products

    def test_clear_products(self, cart, product):
        cart.add_product(product, 20)
        cart.clear()
        assert product not in cart.products

    def test_get_total_price_product(self, cart, product):
        cart.add_product(product, 5)
        assert cart.get_total_price() == 500

    def test_buy(self, product, cart):
        cart.add_product(product, 10)
        cart.buy()
        assert product.quantity == 990

    def test_trying_buy_more_than_possible(self, product, cart):
        cart.add_product(product, 1010)
        with pytest.raises(ValueError):
            cart.buy()
