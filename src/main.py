class Category:
    def __init__(self, name, description='', products=None):
        self.name = name
        self.description = description
        self.total_categories = 0
        self.unique_products = set()
        self._products = []
        if products is not None:
            self._products = products

    def add_product(self, product):
        self._products.append(product)
        self.unique_products.add(product)
        self.total_categories += 1

    def get_all_products(self):
        return self._products

    @property
    def total_unique_products(self):
        return len(self.unique_products)

    def clear_data(self):
        self._products = []
        self.unique_products = set()
        self.total_categories = 0

    def list_products(self):
        for product in self._products:
            print(f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.')


class Product:
    def __init__(self, name, description='', price=0, quantity=0):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Цена должна быть больше 0р")
        self._price = value

    def create_product(self, name, description='', price=0, quantity=0):
        new_product = Product(name, description, price, quantity)
        return new_product



electronics_category = Category('Электроника')
furniture_category = Category('Мебель')

# Создание продуктов
tv = Product.create_product('Телевизор Samsung QLED', 'Телевизор с разрешением 4K', 69999, 99999, 5)
sofa = Product.create_product('Диван', 'Комфортный диван для гостиной', 39999, 24999, 15)
chair = Product.create_product('Кресло', 'Кресло для отдыха', 19999, 17900, 6)

# Добавление продуктов в категории
electronics_category.add_product(tv)
furniture_category.add_product(sofa)
furniture_category.add_product(chair)

print("Всего категорий:", electronics_category.total_categories + furniture_category.total_categories)
print("Уникальные продукты:", electronics_category.total_unique_products + furniture_category.total_unique_products)

# Вывод списка товаров в категориях
electronics_category.list_products()
furniture_category.list_products()
