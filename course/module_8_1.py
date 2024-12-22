# -*- coding: utf-8 -*-
# Задание "Программистам всё можно"

def add_everything_up(a, b):
    if ((isinstance(a, str) and isinstance(b, (int, float))) or
            (isinstance(a, (int, float)) and isinstance(b, str))):
        return f"{a}{b}"
    return a + b


try:
    print(add_everything_up(123.456, 'строка'))
except TypeError as exc:
    print(type(exc), exc)

try:
    print(add_everything_up('яблоко', 4215))
except TypeError as exc:
    print(type(exc), exc)

try:
    print(f"{add_everything_up(123.456, 7):.3f}")
except TypeError as exc:
    print(type(exc), exc)
