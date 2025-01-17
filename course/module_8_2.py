# -*- coding: utf-8 -*-
# Задача "План перехват"


def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        if isinstance(i, (int, float)):
            result += i
        else:
            incorrect_data += 1
            print(f"Некорректный тип данных для подсчёта суммы - {i}")
    return result, incorrect_data


def calculate_average(numbers):
    if not isinstance(numbers, (list, tuple)):
        print('В numbers записан некорректный тип данных')
        return None
    sum, incorrect_data = personal_sum(numbers)
    correct_data = len(numbers) - incorrect_data
    if correct_data > 0:
        return sum / correct_data
    else:
        return 0


try:
    # Строка перебирается, но каждый символ - строковый тип
    print(f'Результат 1: {calculate_average(tuple("1, 2, 3"))}')
except (TypeError, ZeroDivisionError) as exc:
    print(type(exc), exc)

try:
    # Учитываются только 1 и 3
    print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
except (TypeError, ZeroDivisionError) as exc:
    print(type(exc), exc)

try:
    # Передана не коллекция
    print(f'Результат 3: {calculate_average(567)}')
except (TypeError, ZeroDivisionError) as exc:
    print(type(exc), exc)

try:
    # Всё должно работать
    print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
except (TypeError, ZeroDivisionError) as exc:
    print(type(exc), exc)
