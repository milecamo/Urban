# -*- coding: utf-8 -*-
# Задача "Потоки гостей в кафе"

from queue import Queue
from threading import Thread
from random import randint
from time import sleep


class Table:
    def __init__(self, number: int):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = list(tables)

    def guest_arrival(self, *guests):
        for guest in guests:
            put_guest_in_queue = True
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    table.guest.start()
                    print(f"{guest.name} сел(-а) за стол номер {table.number}\n", end='')
                    put_guest_in_queue = False
                    break
            if put_guest_in_queue:
                self.queue.put(guest)
                print(f"{guest.name} в очереди\n", end='')

    def discuss_guests(self):
        while not self.queue.empty() or not all(table.guest is None for table in self.tables):
            for table in self.tables:
                if not table.guest is None and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)\n", end='')
                    print(f"Стол номер {table.number} свободен\n", end='')
                    table.guest = None
            if not self.queue.empty():
                for table in self.tables:
                    if table.guest is None:
                        if not self.queue.empty():
                            table.guest = self.queue.get()
                            print(f"{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}\n",
                                  end='')
                            table.guest.start()
                        else:
                            break


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
                ]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
