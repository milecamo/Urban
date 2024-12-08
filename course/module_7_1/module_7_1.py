# Задача "Учёт товаров"

class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

    def __eq__(self, other):
        return self.name == other.name


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        with open(self.__file_name, 'a') as _:
            pass
        with open(self.__file_name) as file:
            file_data = file.read()
        return file_data

    def add(self, *products):
        file_data = self.get_products()
        file_strings = file_data.split('\n')
        products_base = []
        for file_string in file_strings:
            product_data = file_string.split(', ')
            if len(product_data) > 1:
                product = Product(product_data[0], product_data[1], product_data[2])
                products_base.append(product)

        with open(self.__file_name, 'a') as file:
            for product in products:
                if isinstance(product, Product):
                    if product in products_base:
                        print(f'Продукт {product.name} уже есть в магазине')
                    else:
                        file.write(f'{product}\n')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
