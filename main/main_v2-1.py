print("Добро пожаловать в чалькулятор(v2.1!!!!!)!1!11!1!!!!!")
from math import sqrt

def numbers():
    while True:
        try:
            a = float(input("Введите значение первой переменной: "))
            b = float(input("Введите значение второй переменной: "))
        except (ValueError, TypeError, OverflowError):
            print("Ошибка: Введено НЕ-число либо недействительное значение")
            continue
        return a, b
    
def number():
    while True:
        try:
            c = float(input("Введите значение вычисляемой переменной: "))
        except (ValueError, TypeError, OverflowError):
            print("Ошибка: Введено НЕ-число либо недействительное значение")
            continue
        return c

def mySum():
    a, b = numbers()
    print(a + b)

def myDif():
    a, b = numbers()
    print(a - b)

def myTim():
    a, b = numbers()
    print(a * b)

def myDiv():
    while True:
        try:
            a, b = numbers()
            r = a / b
        except (ZeroDivisionError):
            print("На ноль делить можно...но не в обычном калькуляторе!")
            continue
        else:
            print(r)
            break

def myPow():
    while True:
        try:
            a, b = numbers()
            r = a ** b
        except (OverflowError):
            print("ОшибкОооо: результат слишком большой")
            continue
        else:
            print(r)
            break

def mySqrt():
    while True:
        try:
            c = number()
            r = sqrt(c)
        except (ValueError):
            print("Корень из отрицательного числа...? Интересно...но, нет")
            continue
        else:
            print(r)
            break

while True:
    print("\nДоступные операции(только аккуратно, много try/except'ов): \n1. Сложение \n2. Вычитание \n3. Умножение \n4. Деление \n5. Возведение в степень \n6. Корень из числа")
    print("\nВыход из программы: введите число в номере операции - '69'")
    o = {
        1: mySum,
        2: myDif,
        3: myTim,
        4: myDiv,
        5: myPow,
        6: mySqrt
    }
    try:
        t = int(input("Введите номер операции: "))
    except (TypeError, ValueError):
        print("Ошибка: Введено НЕ-число либо недействительное значение")
        continue
    else:
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