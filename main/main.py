print("Добро пожаловать в чалькулятор!1!11!1!!!!!")
import math as m

def mySum():
    while True:
        try:
            a = float(input("Введите значение первой переменной: "))
            b = float(input("Введите значение второй переменной: "))
        except (ValueError, TypeError, OverflowError):
            print("Ошибка: Введено НЕ-число либо недействительное значение")
            continue
        else:
            print("Сумма: ", a + b)
            break

def myDif():
    while True:
        try:
            a = float(input("Введите значение первой переменной: "))
            b = float(input("Введите значение второй переменной: "))
        except (ValueError, TypeError, OverflowError):
            print("Ошибка: Введено НЕ-число либо недействительное значение")
            continue
        else:
            print("Разность: ", a - b)
            break

def myTim():
    while True:
        try:
            a = float(input("Введите значение первой переменной: "))
            b = float(input("Введите значение второй переменной: "))
        except (ValueError, TypeError, OverflowError):
            print("Ошибка: Введено НЕ-число либо недействительное значение")
            continue
        else:
            print("Произведение: ", a * b)
            break

def myDiv():
    while True:
        try:
            a = float(input("Введите значение первой переменной: "))
            b = float(input("Введите значение второй переменной: "))
            if b == 0:
                print("На ноль делить можно...но не в обычном калькуляторе!")
                continue
        except (ValueError, TypeError, OverflowError):
            print("Ошибка: Введено НЕ-число либо недействительное значение")
            continue
        else:
            print("Частное: ", a / b)
            break

def myPow():
    while True:
        try:
            a = float(input("Введите значение первой переменной: "))
            b = float(input("Введите значение второй переменной: "))
        except (ValueError, TypeError, OverflowError):
            print("Ошибка: Введено НЕ-число либо недействительное значение")
            continue
        else:
            print("Результат степени: ", a ** b)
            break

def mySqrt():
    while True:
        try:
            a = float(input("Введите значение вычисляемого числа: "))
            if a < 0:
                print("В этом калькуляторе нельзя извлечь корень из отрицательного числа! =P")
                continue
        except (ValueError, TypeError, OverflowError):
            print("Ошибка: Введено НЕ-число либо недействительное значение")
            continue
        else:
            print("Корень: ", m.sqrt(a))
            break

while True:
    print("\nДоступные операции(только аккуратно, много try/except'ов): \n1. Сложение \n2. Вычитание \n3. Умножение \n4. Деление \n5. Возведение в степень \n6. Корень из числа")
    print("\nВыход из программы: введите число в номере операции - '69'")
    try:
        c = int(input("Введите номер операции: "))
    except (ValueError, TypeError, OverflowError):
        print("Ошибка: Введено НЕ-число либо недействительное значение. Номер операции обозначается целым(не дробным) числом!")
        continue
    else:
        if c == 0:
            print("Hello, World! Пасхалка")
            continue
        if c == 1:
            mySum()
            continue
        if c == 2:
            myDif()
            continue
        if c == 3:
            myTim()
            continue
        if c == 4:
            myDiv()
            continue
        if c == 5:
            myPow()
            continue
        if c == 6:
            mySqrt()
            continue
        if c == 69:
            break
        else:
            print("ОшибкО: Введённое число выходит за пределы доступных операций!")
            continue