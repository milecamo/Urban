# "Пространство имен"

def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


# NameError: имя 'inner_function' не определено
inner_function()
