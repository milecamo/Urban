# "Пространство имен"

def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


# NameError: имя 'inner_function' не определено
inner_function()

# !!!
# Please see module_4_hard.py Best Time to Buy and Sell Stock
# https://github.com/milecamo/Urban/blob/master/course/module_4_hard.py
