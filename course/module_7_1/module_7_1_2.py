# Задача "Учёт товаров"

import os


class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

    def __eq__(self, other):
        if isinstance(other, Product):
            # по условиям задачи проверку наличия продукта в файле нужно делать по названию
            return self.name == other.name
            # return (self.name == other.name and
            #         self.weight == other.weight and
            #         self.category == other.category)
        return NotImplemented


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
        self.__products_base = []
        self.__file_is_read = False
        self.__products = ''

    def __append(self, product: Product):
        self.__products_base.append(product)
        self.__products += f'{product}\n'

    def __reset(self):
        self.__file_is_read = False
        self.__products = ''

    def get_products(self):
        if not self.__file_is_read:
            self.__products_base = []
            if os.path.exists(self.__file_name) and os.path.isfile(self.__file_name):
                file = open(self.__file_name)
                file_data = file.read()
                file.close()
                for product_string in file_data.split('\n'):
                    if product_string:
                        product_data = product_string.split(',')
                        self.__append(Product(product_data[0], float(product_data[1]), product_data[2]))
            self.__file_is_read = True
        return self.__products

    def add(self, *products):
        self.get_products()
        for product in products:
            if isinstance(product, Product):
                if product in self.__products_base:
                    print(f'Продукт {product.name} уже есть в магазине')
                else:
                    self.__append(product)
                    # self.__reset()
                    file = open(self.__file_name, 'a')
                    file.write(str(product).replace(' ', '') + '\n')
                    file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
