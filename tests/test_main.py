import pytest

from builtins import len
from src.main import Category, Product, Smartphone, ObjectCriationLoggerMixin



@pytest.fixture
def category():
    return Category('Электроника', 'Техника для дома и офиса')


@pytest.fixture
def product(category):
    return Product('Телефон', 'Apple', 10000, 20, 'Современный смартфон', category)


@pytest.fixture
def smartphone(category):
    return Smartphone('iPhone X', 'Смартфон Apple', 50000, 15, 'Apple', category, 'Высокая', 'X', '128 GB', 'Черный')


# Тесты для класса Category
def test_add_product_to_category(category, product):
    category.add_product(product)
    assert product in category.get_all_products()
    assert product in category.unique_products
    assert len(category.get_all_products()) == 1
    assert category.total_categories == 1
    with pytest.raises(TypeError):
        category.add_product('Не продукт')


def test_remove_product_from_category(category, product):
    category.add_product(product)
    category.remove_product(product)
    assert len(category.get_all_products()) == 0
    with pytest.raises(ValueError):
        category.remove_product('Некорректный продукт')


def test_clear_data(category, product):
    category.clear_data()
    category.add_product(product)
    assert len(category.get_all_products()) > 0
    category.clear_data()
    assert len(category.get_all_products()) == 0


def test_list_products(category, product, capsys):
    category.list_products()
    captured = capsys.readouterr()
    output = captured.out.strip()
    expected_output = ""
    assert output == expected_output

    category.add_product(product)
    category.list_products()
    captured = capsys.readouterr()
    output = captured.out.strip()
    expected_output = f"Телефон, 10000 руб. Остаток: 20 шт."
    assert output == expected_output


def test_total_unique_products(category):
    product_1 = Product('Ноутбук', 'Портативный компьютер', 30000, 30, 'Lenovo', category)
    product_2 = Product('Планшет', 'Таблетка', 15000, 40, 'Samsung', category)

    category.add_product(product_1)
    category.add_product(product_2)
    assert len(set([product_1, product_2])) == category.total_unique_products


def test_str_representation(category):
    expected_string = 'Электроника, количество продуктов: 0 шт.'
    assert str(category) == expected_string


# Тесты для класса Product
def test_product_init(product):
    assert product.name == 'Телефон'
    assert product.description == 'Современный смартфон'
    assert product.price == 10000
    assert product.quantity == 20
    assert product.manufacturer == 'Apple'

def test_iadd(product):
    another_product = Product("Другое устройство", "", 2000, 50, "Another Manufacturer", "")
    result = product + another_product
    expected_result = 300000
    assert result == expected_result

    with pytest.raises(TypeError):
        product + "Not a product"


def test_cost_property(product):
    cost = product.cost
    assert cost == 200000


def test_set_cost_invalid_value(product):
    with pytest.raises(ValueError):
        product.cost = -1

    def test_repr(product):
        repr_string = repr(product)
        expected_repr = "Product('Телефон', 'Современный смартфон', 10000, 20)"
        assert repr_string == expected_repr

    def test_add_method(product):
        second_product = Product(
            'Другой телефон',
            'Еще один современный смартфон',
            8000,
            25,
            'Samsung',
            category
        )
        total_cost = product.add(second_product)
        expected_cost = 320000
        assert total_cost == expected_cost

    def test_create_product(product):
        new_product = product.create_product('Новый товар', 'Описания нет', 7000, 35)
        assert new_product.name == 'Новый товар'
        assert new_product.description == 'Описания нет'
        assert new_product.price == 7000
        assert new_product.quantity == 35

        # Тесты для класса Smartphone

    def test_smartphone_init(smartphone):
        assert smartphone.name == 'iPhone X'
        assert smartphone.description == 'Смартфон Apple'
        assert smartphone.price == 50000
        assert smartphone.quantity == 15
        assert smartphone.manufacturer == 'Apple'
        assert smartphone.category == 'Электроника'
        assert smartphone.performance == 'Высокая'
        assert smartphone.model == 'X'
        assert smartphone.storage_capacity == '128 GB'
        assert smartphone.color == 'Черный'

        # Дополнительные тесты для класса Product

    def test_product_quantity_update(product):
        initial_quantity = product.quantity
        product.quantity += 10
        assert product.quantity == initial_quantity + 10

    def test_product_price_update(product):
        initial_price = product.price
        product.price *= 1.05  # Увеличение цены на 5%
        assert product.price == round(initial_price * 1.05)

    def test_product_description_update(product):
        new_description = "Обновленное описание"
        product.description = new_description
        assert product.description == new_description

        # Дополнительные тесты для класса Smartphone

    def test_smartphone_color_change(smartphone):
        smartphone.color = "Красный"
        assert smartphone.color == "Красный"

    def test_smartphone_storage_capacity_update(smartphone):
        smartphone.storage_capacity = "256 GB"
        assert smartphone.storage_capacity == "256 GB"

    def test_smartphone_model_update(smartphone):
        smartphone.model = "XS"
        assert smartphone.model == "XS"

        # Тесты для миксина ObjectCriationLoggerMixin

    def test_object_creation_logger_mixin():
        class TestClass(ObjectCriationLoggerMixin):
            def __init__(self, a, b=1):
                super().__init__(a, b=b)

        obj = TestClass(42)
        obj2 = TestClass(7, b='hello')
