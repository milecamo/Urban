print("Проверим сколько чисел равны между собой")
first, second, third = (
    map(int, input("Введите три целых числа через запятую: ").split(',')))

if first == second == third:
    print("Ответ: ", 3)
elif (first == second or
      second == third or
      first == third):
    print("Ответ: ", 2)
else:
    print("Ответ: ", 0)
