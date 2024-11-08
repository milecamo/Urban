# Задание "Раз, два, три, четыре, пять .... Это не всё?"

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(*args):
    result = 0
    for i in args:
        if isinstance(i, int):
            result += i
        elif isinstance(i, str):
            result += len(i)
        elif isinstance(i, dict):
            result += calculate_structure_sum(*i.keys())
            result += calculate_structure_sum(*i.values())
        else:
            result += calculate_structure_sum(*i)
    return result


result = calculate_structure_sum(data_structure)
print(result)
