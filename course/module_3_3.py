# Задача "Распаковка"

def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [2, 'hi', False]
values_dict = {'a': 3, 'b': 'bye', 'c': 1.0}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['i', True]
print_params(*values_list_2, 42)
