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
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только продукты или их наследников")


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

    def __iadd__(self, other):
        if not  isinstance(other, type(self)):
            raise TypeError(f'Нельзя складывать товары из разных классов: {type(self)} и {type(other)}.')
        return f'{self.name} + {other.name}'

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

class Smartphone(Product):
    def __init__(self, name, description='', price=0, quantity=0, performance=0.0, model='', storage_capacity=0,
                 color=''):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.storage_capacity = storage_capacity
        self.color = color

    def str(self):
        return (f"{self.name}, {self.description}, {self.price} руб., {self.quantity} шт.\n"
                f"Производительность: {self.performance}\n"
                f"Модель: {self.model}\n"
                f"Встроенная память: {self.storage_capacity} ГБ\n"
                f"Цвет: {self.color}")

class Grass(Product):
    def __init__(self, name, description='', price=0, quantity=0, country_of_origin='', germination_time=0,
                 color=''):
        super().__init__(name, description, price, quantity)
        self.country_of_origin = country_of_origin
        self.germination_time = germination_time
        self.color = color

    def str(self):
        return (f"{self.name}, {self.description}, {self.price} руб., {self.quantity} шт.\n"
                f"Страна производитель: {self.country_of_origin}\n"
                f"Срок прорастания: {self.germination_time} дней\n"
                f"Цвет: {self.color}")


all_category = []
electronics_category = Category('Электроника')
all_category.append(electronics_category)
furniture_category = Category('Мебель')
all_category.append(furniture_category)
garden_category = Category('Садовые товары')
all_category.append(garden_category)


# Создание продуктов
#Телефоны
iphone_13 = Smartphone(
    name='Iphone 13',
    description= 'Флагман от Apple',
    price= 100000,
    quantity=25,
    performance=9.8,
    model='iphone 13',
    storage_capacity=512,
    color='Graphite'
)
samsung_a12 = Smartphone(
    name='Samsung_a12',
    description='взрывной смартфон',
    price=5000,
    quantity=256,
    color='Blue Sky'
)
#Травы
premium_grass_mix = Grass(
    name='Премиум газонная трава',
    description='Смесь высококачественных сортов газонных трав',
    price=2500,
    quantity=40,
    country_of_origin='Германия',
    germination_time=14,
    color='Темно-зеленый'
)
eco_lawn= Grass(
    name='Эко-газон',
    description='Экольогичная смесь газонных трав',
    price=1800,
    quantity=60,
    country_of_origin='Россия',
    germination_time=18,
    color='Светло-зеленая'
)
tv = Product.create_product('Телевизор Samsung QLED', 'Телевизор с разрешением 4K', 123456, 99999, 670)
sofa = Product.create_product('Диван', 'Комфортный диван для гостиной', 5648156, 24999, 1500)
chair = Product.create_product('Кресло', 'Кресло для отдыха', 456814454, 17900, 800)

# Добавление продуктов в категории
electronics_category.add_product(iphone_13)
electronics_category.add_product(samsung_a12)
electronics_category.add_product(tv)
garden_category.add_product(premium_grass_mix)
garden_category.add_product(eco_lawn)
furniture_category.add_product(sofa)
furniture_category.add_product(chair)

#подсчет количества общей цены продукции на складе
all_products_price = chair.price * chair.quantity + sofa.price * sofa.quantity + tv.price * tv.quantity + iphone_13.price * iphone_13.quantity + samsung_a12.price * samsung_a12.quantity + premium_grass_mix.price * premium_grass_mix.quantity + eco_lawn.price * eco_lawn.quantity

print(f"Всего категорий: {all_category.__len__()}")
print("Уникальные продукты:", electronics_category.__len__() + furniture_category.__len__() + garden_category.__len__())
# Вывод списка товаров в категориях
electronics_category.list_products()
garden_category.list_products()
furniture_category.list_products()

print(f'Садовые товары, количество продуктов: {garden_category.__len__()}')
print(f'Электроника, количество продуктов: {electronics_category.__len__()}')
print(f'Мебель, количество продуктов: {furniture_category.__len__()}')
print(f'Всего на складе продукции на {all_products_price}р')
