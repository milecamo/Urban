# -*- coding: utf-8 -*-
# Задача "Многопроцессное считывание"

from multiprocessing import Pool
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name) as file:
        line = True
        while line:
            line = file.readline()
            all_data.append(line)


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный вызов 0:00:04.988363 (линейный)
    linecall_start = datetime.now()
    for filename in filenames:
        read_info(filename)
    print(f'{datetime.now() - linecall_start} (линейный)\n', end='')

    # Многопроцессный 0:00:02.289052 (многопроцессный)
    time_start = datetime.now()
    with Pool(4) as p:
        p.map(read_info, filenames)
    print(f'{datetime.now() - time_start} (многопроцессный)\n', end='')