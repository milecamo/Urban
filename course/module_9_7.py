# -*- coding: utf-8 -*-
# Задание по теме "Декораторы"

from sympy import isprime


def is_prime(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if isprime(res):
            print("Простое")
        else:
            print("Составное")
        return res

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
