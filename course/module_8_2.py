# Задача "План перехват"


def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data += i
    return (result, incorrect_data)


def calculate_average(numbers):
    try:
        return personal_sum(numbers)/len(numbers)
    except ZeroDivisionError:
        return 0
