print("Добро пожаловать в чалькулятор(v2.3!!!!!)")
from math import sqrt

class InputOutput:
    """Класс создаёт объекты с принимаемым значением на входе"""
    def __init__(self, value=None):
        self.value = value

    @staticmethod
    def get_number(num_type, prompt, error=None):
        while True:
            try:
                return num_type(input(prompt))
            except(TypeError, ValueError, OverflowError):
                if error:
                    print(error)
                else:
                    print("ОшибкО: Введено недействительное значение переменной!")
    
class MathOperations:
    """Класс по вычислению математических операций"""
    @staticmethod
    def ee():
        print("Hello, World! Пасхалка")

    @staticmethod
    def exit():
        return 1 / 0
    
    @staticmethod
    def my_add(num1, num2):
        print(f"Сумма: {num1} + {num2} = {num1 + num2}")
        return num1 + num2
    
    @staticmethod
    def my_dif(num1, num2):
        print(f"Разность: {num1} - {num2} = {num1 - num2}")
        return num1 - num2
    
    @staticmethod
    def my_mul(num1, num2):
        print(f"Произведение: {num1} * {num2} = {num1 * num2}")
        return num1 * num2
    
    @staticmethod
    def my_div(num1, num2):
        if num2 == 0:
            print("На ноль делить можно...но мы же не занимаемся высшей математикой!")
            return None
        print(f"Частное: {num1} / {num2} = {num1 / num2}")
        return num1 / num2
    
    @staticmethod
    def my_pow(num1, num2):
        while True:
            try:
                print(f"Результат степени: {num1} ^ {num2} = {num1 ** num2}")
                return num1 ** num2
            except(OverflowError):
                print("Результат ОЧЕНЬ большоооооооооой!!!!!")
                return None

    @staticmethod        
    def my_sqrt(num):
        if num < 0:
            print(f"Корень из отрицательного числа...? Ладно, вот корявый результат: {num ** -0.5}")
            return None
        print(f"Результат корня: {sqrt(num)}")
        return sqrt(num)

#Ярлыки классов для удобства
io = InputOutput
mo = MathOperations
#Объекты со значениями состояния
a = InputOutput()
b = InputOutput()
result = InputOutput()
#Отдельно вынес словари...потому что я люблю Python-Qython
c_variants_positive = ["Да", "дА", "ДА", "да", "1", 1]
c_variants_negative = ["Нет", "нЕт", "неТ", "НеТ", "нЕТ", "НЕт", "НЕТ", "нет", "2", 2]

class Main:
    operations = {
        0: mo.ee,
        1: mo.my_add,
        2: mo.my_dif,
        3: mo.my_mul,
        4: mo.my_div,
        5: mo.my_pow,
        6: mo.my_sqrt,
        7: mo.exit
    }
    
    @staticmethod
    def handle_result(arg=0):
        if result.value:
            if arg == 0:
                print("Использовать использовать значение результата последней выполненной операции? \n1. Да \n2. Нет")
                while True:
                    c = io.get_number(str, "Выбор: ", "Недействительное значение!")
                    if c in c_variants_positive:
                        print("Какой из переменных(значение выбранной переменной будет перезаписано) присвоить значение последнего результата? Для примера: a + b = c \n1. Переменной 'a' \n2. Переменной 'b'")
                        while True:
                            r = io.get_number(str, "> ", "Недействительное значение!")
                            if r == "a" or r == "1":
                                a.value = result.value
                                return
                            elif r == "b" or r == "2":
                                b.value = result.value
                                return
                            else:
                                print("Недействительное значение выбора!")
                                continue
                    elif c in c_variants_negative:
                        result.value = None
                        return None
                    else:
                        print("Недействительное значение выбора!")
                        continue
            elif arg == 1:
                print("Использовать использовать значение результата последней выполненной операции? \n1. Да \n2. Нет")
                while True:
                    c = io.get_number(str, "Выбор: ", "Недействительное значение!")
                    if c in c_variants_positive:
                        a.value = result.value
                        return
                    elif c in c_variants_negative:
                        result.value = None
                        return
                    else:
                        print("Недействительное значение выбора!")
                        continue
            else:
                print("Недействительное значение аргумента!")
                return None

    while True:
        a.value = 0
        b.value = 0

        choice = io.get_number(int, "\nВыберите операцию(по номеру из доступных): \n1. Сложение \n2. Вычитание \n3. Умножение \n4. Деление \n5. Возведение в степень \n6. Корень из числа \n7. Выход из программы \n> ", "Недействительный номер!")
        if choice not in operations:
            print("Такой операции нет!")
            continue

        elif operations[choice] is mo.exit:
            mo.exit()

        elif operations[choice] is mo.ee:
            mo.ee()

        elif operations[choice] is mo.my_sqrt:
            if result.value:
                handle_result(1)
                if result.value == None:
                    a.value = io.get_number(float, "Введите значение числа: ")
                result.value = operations[choice](a.value)
            else:
                a.value = io.get_number(float, "Введите значение числа: ")
                result.value = operations[choice](a.value)

        elif result.value:
            handle_result()
            if a.value == result.value and a.value != None:
                b.value = io.get_number(float, "Введите значение переменной b: ")
            elif b.value == result.value and a.value != None:
                a.value = io.get_number(float, "Введите значение переменной a: ")
            else:
                a.value = io.get_number(float, "Введите значение переменной a: ")
                b.value = io.get_number(float, "Введите значение переменной b: ")
            result.value = operations[choice](a.value, b.value)

        else:
            a.value = io.get_number(float, "Введите значение переменной a: ")
            b.value = io.get_number(float, "Введите значение переменной b: ")
            result.value = operations[choice](a.value, b.value)
