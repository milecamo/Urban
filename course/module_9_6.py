# -*- coding: utf-8 -*-
# Задание по теме "Генераторы"

def all_variants(text):
    for length in range(1, len(text) + 1):
        for position in range(len(text) - length + 1):
            yield text[position:position + length]


a = all_variants("abc")
for i in a:
    print(i)
