# Задание "Программистам всё можно"

def add_everything_up(a, b):
    if ((isinstance(a, str) and isinstance(b, (int, float))) or
            (isinstance(a, (int, float)) and isinstance(b, str))):
        return f"{a}{b}"
    try:
        return a + b
    except TypeError:
        pass


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
