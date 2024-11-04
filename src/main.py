from abc import ABC, abstractclassmethod
from unicodedata import category


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
        #создаем ограничение для "корзины" если товар отсутствует на "складе"
        #выдаст ошибку с текстом: "Нельзя добавить товар которого нет на складе"
        if product.quantity == 0:
            raise ValueError("Нельзя добавить товар которого нет на складе")

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

class ObjectCriationLoggerMixin:
    def __init__(self):
        print(repr(self))

#добавлен магический метод __repr__
    def __repr__(self):
        args_str = ', '.join(map(str, args))
        kwargs_str = ', '.join(f'{k}={v}' for k, v in kwargs.items())

        all_args = ', '.join([args_str, kwargs_str])

        if not all_args:
            all_args = ''

class AbstractProduct(ABC):
    def __init__(self, name, manufacturer, quantity, description):
        self.name = name
        self.manufacturer = manufacturer
        self.quantity = quantity
        self.description = description

        @abstractclassmethod
        def get_description(self):
            pass

class Product(AbstractProduct):
    def __init__(self, name, description, price, quantity, manufacturer, category):
        super().__init__(name, description, quantity, manufacturer)
        self.price = price
        self.category = category

    def get_description(self):
        return f"{self.name} (OT {self.category}, price: {self.price})"

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

    def create_product(self, name, description, price, quantity):
        new_product = Product(name, description, price, quantity)
        return new_product

class Smartphone(Product):
    def __init__(self, name, description, price, quantity, manufacturer, category, performance, model, storage_capacity,
                 color=''):
        super().__init__(name, description, price, quantity, manufacturer, category)
        self.performance = performance
        self.model = model
        self.storage_capacity = storage_capacity
        self.color = color

    def str(self):
        return (f"{self.category}, {self.name}, {self.description}, {self.price} руб., {self.quantity} шт.\n"
                f"Производительность: {self.performance}\n"
                f"Производитель: {self.manufacturer}"
                f"Модель: {self.model}\n"
                f"Встроенная память: {self.storage_capacity} ГБ\n"
                f"Цвет: {self.color}")

class Grass(Product):
    def __init__(self, name='', description='', price=0, quantity=0, manufacturer='', category='', germination_time=0,
                 color=''):
        super().__init__(name, description, price, quantity, manufacturer, category)
        self.germination_time = germination_time
        self.color = color

    def str(self):
        return (f"{self.name}, {self.description}, {self.price} руб., {self.quantity} шт.\n"
                f"Страна производитель: {self.manufacturer}\n"
                f"Срок прорастания: {self.germination_time} дней\n"
                f"Цвет: {self.color}")


all_category = []
electronics_category = Category('Электроника')
all_category.append(electronics_category)

garden_category = Category('Садовые товары')
all_category.append(garden_category)


# Создание продуктов
#Телефоны
iphone_13 = Smartphone(
    category="Смартфон",
    manufacturer="США",
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
    category="Смартфон",
    manufacturer="Южная Корея",
    name='Samsung_a12',
    description='взрывной смартфон',
    price=5000,
    performance=7.2,
    model='Samsung a12',
    storage_capacity=64,
    quantity=12,
    color='Blue Sky'
)
try:
    smartphone_zero = Smartphone(
        category="Смартфон",
        manufacturer="Южная Корея",
        name='Samsung_a22',
        description='взрывной смартфон',
        price=7000,
        performance=8.4,
        model='Samsung a22',
        storage_capacity=64,
        quantity=0,
        color='Blue Sky'
    )

    electronics_category.add_product(smartphone_zero)
except ValueError as e:
    print(e)#cообщение об ошибке


#Травы
premium_grass_mix = Grass(
    category="Газон для сада",
    name='Премиум газонная трава',
    description='Смесь высококачественных сортов газонных трав',
    price=2500,
    quantity=40,
    manufacturer='Германия',
    germination_time=14,
    color='Темно-зеленый'
)
eco_lawn= Grass(
    category="Газон для сада",
    name='Эко-газон',
    description='Экольогичная смесь газонных трав',
    price=1800,
    quantity=60,
    manufacturer='Россия',
    germination_time=18,
    color='Светло-зеленая'
)

# Добавление продуктов в категории
electronics_category.add_product(iphone_13)
electronics_category.add_product(samsung_a12)
#try:



garden_category.add_product(premium_grass_mix)
garden_category.add_product(eco_lawn)


#подсчет количества общей цены продукции на складе
all_phone_price= iphone_13.price * iphone_13.quantity + samsung_a12.price * samsung_a12.quantity
all_garden_price= premium_grass_mix.price * premium_grass_mix.quantity + eco_lawn.price * eco_lawn.quantity
all_products_price = all_garden_price + all_phone_price

print(f"Всего категорий: {all_category.__len__()}")
print("Уникальные продукты:", electronics_category.__len__()  + garden_category.__len__())
# Вывод списка товаров в категориях
electronics_category.list_products()
garden_category.list_products()

print(Product(iphone_13.name, iphone_13.description, iphone_13.price, iphone_13.quantity, iphone_13.manufacturer,
              iphone_13.category))
print(Product(samsung_a12.name, samsung_a12.description, samsung_a12.price, samsung_a12.quantity, samsung_a12.manufacturer,
              samsung_a12.category))
print(Product(premium_grass_mix.name, premium_grass_mix.description, premium_grass_mix.price, premium_grass_mix.quantity, premium_grass_mix.manufacturer,
              premium_grass_mix.category))
print(Product(eco_lawn.name, eco_lawn.description, eco_lawn.price, eco_lawn.quantity, eco_lawn.manufacturer,
              eco_lawn.category))

print(f'Садовые товары, количество продуктов: {garden_category.__len__()}')
print(f'Электроника, количество продуктов: {electronics_category.__len__()}')
print(f'Всего на складе продукции на {all_products_price}р')
