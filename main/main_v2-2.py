print("Добро пожаловать в чалькулятор(v2.2!!!!!)")
from math import sqrt

def get_number(num_type, prompt):
    while True:
        try:
            return num_type(input(prompt))
        except(TypeError, ValueError, OverflowError):
            print("ОшибкО: Введено недействительное значение переменной!")
            continue

def my_sum():
    a, b = get_number(float, "Введите значение первого слагаемого: "), get_number(float, "Введите значение второго слагаемого: ")
    print(f"Сумма: {a} + {b} = {a + b}")

def my_dif():
    a, b = get_number(float, "Введите значение уменьшаемого: "), get_number(float, "Введите значение вычитаемого: ")
    print(f"Разность: {a} - {b} = {a - b}")

def my_tim():
    a, b = get_number(float, "Введите значение первого множителя: "), get_number(float, "Введите значение второго множителя: ")
    print(f"Произведение: {a} * {b} = {a * b}")

def my_div():
    a, b = get_number(float, "Введите значение делимого: "), get_number(float, "Введите значение делителя: ")
    if b == 0:
        print("На ноль делить можно...но не в этом калькуляторе!")
        return None
    print(f"Частное: {a} / {b} = {a / b}")

def my_pow():
    a, b = get_number(float, "Введите значение основания степени: "), get_number(float, "Введите значение показателя степени: ")
    while True:
        try:
            print(f"Результат: {a} ^ {b} = {a ** b}")
        except(OverflowError):
            print("Результат ОЧЕНЬ большоооооооооой!!!!!")
            break
        else:
            break

def my_sqrt():
    a = get_number(float, "Введите значение вычислямого корня: ")
    if a < 0:
        print("Корень из отрицательного числа...? Интересно, ведь у нас не комплексная математика!")
        return None
    print(f"Результат: {sqrt(a)}")

while True:
    print("\nДоступные операции: \n1. Сложение \n2. Вычитание \n3. Умножение \n4. Деление \n5. Возведение в степень \n6. Корень из числа")
    print("\nВыход из программы: введите число в номере выбора операции - '69'")

    o = {
        1: my_sum,
        2: my_dif,
        3: my_tim,
        4: my_div,
        5: my_pow,
        6: my_sqrt
    }

    t = get_number(int, "Выберите выполняемую операцию(номер в списке соответствует операции): ")

    if t == 0:
        print("Hello, World! Пасхалка")
        continue
    elif t == 69:
        break
    elif t in o:
        o[t]()
    else:
        print("ОшибкО: Введённое число выходит за пределы доступных операций!")
        continue