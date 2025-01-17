# -*- coding: utf-8 -*-
# Задача "Потоковая запись в файлы"

from threading import Thread
from time import sleep
from datetime import datetime


def wite_words(word_count, file_name):
    with open(file_name, "w", encoding="utf8") as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            sleep(.1)
    print(f"Завершилась запись в файл {file_name}")


start_time = datetime.now()
wite_words(10, "example1.txt")
wite_words(30, "example2.txt")
wite_words(200, "example3.txt")
wite_words(100, "example4.txt")
print(f"Работа функций {datetime.now() - start_time}")

thread1 = Thread(target=wite_words, args=(10, "example5.txt"))
thread2 = Thread(target=wite_words, args=(30, "example6.txt"))
thread3 = Thread(target=wite_words, args=(200, "example7.txt"))
thread4 = Thread(target=wite_words, args=(100, "example8.txt"))
threads = [thread1, thread2, thread3, thread4]

start_time = datetime.now()
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(f"Работа потоков {datetime.now() - start_time}")
