# Задание "Они все так похожи"

from math import pi, sqrt

DEFAULT_COLOR = (255, 255, 255)


class Figure:
    sides_count = 0

    def __init__(self, color=DEFAULT_COLOR, *sides):
        self.__sides = None
        self.set_sides(*sides)

        self.__color = None
        if hasattr(color, '__iter__') and len(color) == 3:
            self.set_color(*color)
        if not self.__color:
            self.__color = DEFAULT_COLOR

        self.filled = False

    def get_color(self):
        return list(self.__color)

    @staticmethod
    def __is_valid_color(r: int, g: int, b: int):
        for color in (r, g, b):
            if not isinstance(color, int) or color < 0 or color > 255:
                return False
        return True

    def set_color(self, r: int, g: int, b: int):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, *sides):
        if len(sides) != self.sides_count:
            return False
        for side in sides:
            if not isinstance(side, int) or side <= 0:
                return False
        return True

    def get_sides(self):
        return self.__sides.copy()

    def __len__(self):
        result = 0
        for side in self.__sides:
            result += side
        return result

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        if not self.__sides:
            self.__sides = []
            for i in range(self.sides_count):
                self.__sides.append(1)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color=DEFAULT_COLOR, *sides):
        # although we do not must define self.__radius in __init__
        # it could be defined in set_sides()
        self.__radius = 0
        super().__init__(color, *sides)

    def set_sides(self, *new_sides):
        old_side = 0 if not hasattr(self, '__radius') or not self.__radius else self.get_sides()[0]
        # if self.__radius isn't defined in __init__
        # old_side = 0 if not hasattr(self, '__radius') else self.get_sides()[0]

        super().set_sides(*new_sides)
        new_side = self.get_sides()[0]

        if old_side != new_side:
            # if it's not defined in __init__
            # self.__radius will be defined here
            # for the 1st time
            self.__radius = new_side / 2 / pi

    def get_square(self):
        return self.get_sides()[0] ** 2 / 4 / pi

    def get_radius(self):
        return self.__radius


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        sides = self.get_sides()
        p = (sum(sides)) / 2
        return sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))


class Cube(Figure):
    sides_count = 12

    def set_sides(self, *new_sides):
        self.sides_count = 1
        super().set_sides(*new_sides)
        self.sides_count = 12
        # then append 11 more equal sides
        sides = self.get_sides()
        for i in range(self.sides_count - 1):
            sides.append(sides[0])
        super().set_sides(*sides)

    def get_volume(self):
        return self.get_sides()[0] ** 3

    def get_square(self):
        return self.get_sides()[0] ** 2 * 6

    # def __len__(self):
    #     # сумма ребер куба
    #     return self.get_sides()[0] * self.sides_count
    #     # площадь куба
    #     return self.get_square()


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка радиуса (круга)
print(round(circle1.get_radius(), 2))  # 1.59

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
cube1.set_color(-1, 70, 15)  # Не изменится
cube1.set_color(1.0, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра, это и есть длина:
print(len(circle1))

# Проверка объёма, площади и периметра (куба):
print(cube1.get_volume())
print(cube1.get_square())  # 216
print(len(cube1))  # 72

# Проверка радиуса и площади (круга)
print(round(circle1.get_radius(), 2))  # 2.39
print(round(circle1.get_square(), 2))  # 17.9

# triangle1 = Triangle((), 3, 4, 5)
triangle1 = Triangle(1)
triangle1.set_sides(3,4,5)

# Проверка площади (треугольника)
print(round(triangle1.get_square(), 2))  # 6.0
# Проверка цветов:
print(triangle1.get_color())  # [255, 255, 255]
