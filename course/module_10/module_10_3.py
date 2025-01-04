# -*- coding: utf-8 -*-
# Задача "Банковские операции"

import threading
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(0, 100):
            refill = randint(50, 500)
            self.balance += refill
            print(f"Пополнение: {refill}. Баланс: {self.balance}\n", end="")
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)

    def take(self):
        for i in range(0, 100):
            withdrawal = randint(50, 500)
            print(f"Запрос на {withdrawal}\n", end="")
            if withdrawal <= self.balance:
                self.balance -= withdrawal
                print(f"Снятие: {withdrawal}. Баланс: {self.balance}\n", end="")
            else:
                print("Запрос отклонён, недостаточно средств\n", end="")
                self.lock.acquire()
            sleep(0.001)


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
