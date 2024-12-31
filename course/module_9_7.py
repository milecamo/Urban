# -*- coding: utf-8 -*-
# Задание по теме "Декораторы"
from future.utils import raise_
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
def sum_three(*args):
    if len(args) != 3:
        raise TypeError(f"sum_three() takes 3 positional arguments but {len(args)} were given")
    if not all(isinstance(i, (int, float)) for i in args):
        raise TypeError(f"unsupported argument for sum_three(): not 'int' or 'float'")
    return sum(args[:3])


result = sum_three(2, 3, 6)
print(result)
