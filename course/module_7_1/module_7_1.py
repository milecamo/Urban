# Задача "Учёт товаров"

import os


class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        # По условию задачи здесь должны быть пробелы после запятой.
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file_data = ''
        if os.path.exists(self.__file_name) and os.path.isfile(self.__file_name):
            file = open(self.__file_name)
            file_data = file.read()
            file.close()
        return file_data

    def add(self, *products):
        for product in products:
            if isinstance(product, Product):
                # В примере приведен неправильный вывод Shop.get_products(),
                # словно в Shop.add() они используют результат Shop.get_products(),
                # запущенного один раз, перед добавлением всех products.
                # И проверка на продукты с одинаковым названием в переданных products не делается.

                # Правильно конечно и проще использовать результат Shop.get_products()
                # при добавлении каждого продукта, если файл не очень большой.
                product_exist = False
                file_data = self.get_products()
                if file_data:
                    for product_string in file_data.split('\n'):
                        # По условиям задачи проверку наличия продукта в файле
                        # нужно делать по названию.
                        if product.name == product_string[0:product_string.find(',')]:
                            product_exist = True
                            print(f'Продукт {product.name} уже есть в магазине')
                            break
                if not product_exist:
                    file = open(self.__file_name, 'a')
                    # В примере скриншота файла в условиях задачи
                    # все данные в строке разделены запятой с пробелами.
                    # И в примере вывода на консоль результата Shop.get_products()
                    # все данные в строке тоже разделены запятой с пробелами.
                    file.write(f'{product}\n')
                    file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
