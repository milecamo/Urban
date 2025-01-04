# -*- coding: utf-8 -*-
# Задача "За честь и отвагу!"

from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name: str, power: int):
        Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name}, на нас напали!\n", end="")
        warriors = 100
        days = 0
        while warriors > 0:
            sleep(1)
            days += 1
            warriors = 0 if warriors <= self.power else warriors - self.power
            print(f"{self.name} сражается {days} день(дня)..., осталось {warriors} воинов.\n", end="")
        print(f"{self.name} одержал победу спустя {days} дней(дня)!\n", end="")


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

# Вывод строки об окончании сражения
print("Все битвы закончились!")
