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

    def remove_product(self, product):
        self._products.remove(product)
        self.unique_products.discard(product)
        self.total_categories -= 1

    def get_all_products(self):
        return self._products

    @property
    def total_unique_products(self):
        return len(self.unique_products)

    def __len__(self):
        return len(self._products)

    def clear_data(self):
        self._products = []
        self.unique_products = set()
        self.total_categories = 0

    def list_products(self):
        for product in self._products:
            print(f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.')

    def __str__(self):
        return f'{self.name}, количество продуктов: {len(self._products)} шт.'


class Product:
    def __init__(self, name, description='', price=0, quantity=0):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @property
    def cost(self):
        return self.price * self.quantity

    @cost.setter
    def cost(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Стоимость должна быть положительным числом")
        self._cost = value

    def __repr__(self):
        return f"Product({self.name!r}, {self.description!r}, {self.price!r}, {self.quantity!r})"

    def __str__(self):
        return f"{self.name}, {self.description}, {self.price} руб., {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты Product")
        return self.cost + other.cost

    def create_product(self, name, description='', price=0, quantity=0):
        new_product = Product(name, description, price, quantity)
        return new_product


electronics_category = Category('Электроника')
furniture_category = Category('Мебель')

# Создание продуктов
tv = Product.create_product('Телевизор Samsung QLED', 'Телевизор с разрешением 4K', 123456, 99999, 5)
sofa = Product.create_product('Диван', 'Комфортный диван для гостиной', 5648156, 24999, 15)
chair = Product.create_product('Кресло', 'Кресло для отдыха', 456814454, 17900, 6)
#подсчет количества общей цены продукции на складе
all_products_price = chair.price * chair.quantity + sofa.price * sofa.quantity + tv.price * tv.quantity

# Добавление продуктов в категории
electronics_category.add_product(tv)
furniture_category.add_product(sofa)
furniture_category.add_product(chair)

print("Всего категорий:", electronics_category.total_categories + furniture_category.total_categories)
print("Уникальные продукты:", electronics_category.total_unique_products + furniture_category.total_unique_products)
# Вывод списка товаров в категориях
electronics_category.list_products()
furniture_category.list_products()
print(f'Электроника, количество продуктов: {electronics_category.__len__()}')
print(f'Мебель, количество продуктов: {furniture_category.__len__()}')
print(f'Всего на складе продукции на {all_products_price}р')

