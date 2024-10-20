import pytest

from src.main import Category

from src.main import Product


@pytest.fixture
def setup_category():
    electronics_category = Category('Электроника')
    furniture_category = Category('Мебель')
    yield electronics_category, furniture_category

@pytest.fixture
def setup_products():
    tv = Product('Телевизор Samsung QLED', 'Телевизор с разрешением 4K', 99999, 5)
    sofa = Product('Диван', 'Комфортный диван для гостиной', 24999, 15)
    chair = Product('Кресло', 'Кресло для отдыха', 17900, 6)
    yield tv, sofa, chair

def test_add_products(setup_category, setup_products):
    electronics_category, furniture_category = setup_category
    tv, sofa, chair = setup_products

    electronics_category.add_product(tv)
    electronics_category.add_product(sofa)
    furniture_category.add_product(chair)

    assert electronics_category.total_categories == 2
    assert electronics_category.total_unique_products == 2
    assert furniture_category.total_categories == 1
    assert furniture_category.total_unique_products == 1

def test_clear_data(setup_category, setup_products):
    electronics_category, furniture_category = setup_category
    tv, sofa, chair = setup_products

    electronics_category.add_product(tv)
    electronics_category.add_product(sofa)
    furniture_category.add_product(chair)

    electronics_category.clear_data()
    furniture_category.clear_data()

    assert electronics_category.total_categories == 0
    assert electronics_category.total_unique_products == 0
    assert furniture_category.total_categories == 0
    assert furniture_category.total_unique_products == 0

@pytest.mark.parametrize("name, desc, prod", [
    ("Электроника", "", None),
    ("Мебель", "", None),
])
def test_category_initialization(name, desc, prod):
    category = Category(name, desc, prod)
    assert category.name == name
    assert category.description == desc
    assert category.total_categories == 0
    assert category.unique_products == set()

def test_category_adding_products():
    electronics_category = Category('Электроника')
    furniture_category = Category('Мебель')

    tv = Product('Телевизор Samsung QLED', 'Телевизор с разрешением 4K', 69999, 10)
    sofa = Product('Диван', 'Комфортный диван для гостиной', 39999, 2)
    chair = Product('Кресло', 'Кресло для отдыха', 19999, 3)

    electronics_category.add_product(tv)
    electronics_category.add_product(sofa)
    furniture_category.add_product(chair)

    assert electronics_category.total_categories == 2
    assert electronics_category.total_unique_products == 2
    assert furniture_category.total_categories == 1
    assert furniture_category.total_unique_products == 1

def test_category_clear_data():
    electronics_category = Category('Электроника')
    furniture_category = Category('Мебель')

    tv = Product('Телевизор Samsung QLED', 'Телевизор с разрешением 4K', 69999, 10)
    sofa = Product('Диван', 'Комфортный диван для гостиной', 39999, 2)
    chair = Product('Кресло', 'Кресло для отдыха', 19999, 3)

    electronics_category.add_product(tv)
    electronics_category.add_product(sofa)
    furniture_category.add_product(chair)

    electronics_category.clear_data()
    furniture_category.clear_data()

    assert electronics_category.total_categories == 0
    assert electronics_category.total_unique_products == 0
    assert furniture_category.total_categories == 0
    assert furniture_category.total_unique_products == 0