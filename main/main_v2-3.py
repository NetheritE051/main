print("Добро пожаловать в чалькулятор(v2.3!!!!!)")
from cmath import sqrt
import sys

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
    
    @staticmethod
    def handle_result(res, num1, num2=None):
        if res is not None:
            while True:
                c = input("Использовать результат последней выполненной операции?\n1. Да\n2. Нет\nВыбор: ")
                if c.strip().lower() in ("1", "yes", "да"):
                    if num2 is None:
                        num1.value = res
                        return None
                    while True:
                        r = input("Какой переменной присвоить значение результата?\nДля примера, формула: a + b = c\n1. Переменной 'a'\n2. Переменной 'b'\nВыбор: ")
                        if r.strip().lower() in ("1", "a", "а"):
                            num1.value = res
                            return "a"
                        elif r.strip().lower() in ("2", "b", "б"):
                            num2.value = res
                            return "b"
                        else:
                            print("Недействительное значение выбора!")
                            continue
                elif c.strip().lower() in ("2", "no", "нет"):
                    return None
                else:
                    print("Нет такого выбора!")
                    continue
        else:
            return None
    
class MathOperations:
    """Класс по вычислению математических операций"""
    @staticmethod
    def ee():
        print("Hello, World! Пасхалка")
    
    @staticmethod
    def shutdown():
        sys.exit("Выход из программы...")
    
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
        try:
            print(f"Произведение: {num1} * {num2} = {num1 * num2}")
            return num1 * num2
        except OverflowError:
            print("Результат ОЧЕНЬ большой!")
            return None
    
    @staticmethod
    def my_div(num1, num2):
        if num2 == 0:
            print("На ноль делить можно...но мы же не занимаемся высшей математикой!")
            return None
        print(f"Частное: {num1} / {num2} = {num1 / num2}")
        return num1 / num2
    
    @staticmethod
    def my_pow(num1, num2):
        try:
            print(f"Результат степени: {num1} ^ {num2} = {num1 ** num2}")
            return num1 ** num2
        except OverflowError:
            print("Результат СЛИШКОМ большоооооооооой!!!!!")
            return None
    
    @staticmethod        
    def my_sqrt(num):
        print(f"Результат корня: {sqrt(num)}")
        return sqrt(num)

class Main:
    #Класс для экспериментов и тестов ядерного кода
    #Ярлыки классов для удобства
    IO = InputOutput
    MO = MathOperations

    a, b, result = IO(0), IO(0), IO(None)

    operations = {
        0: MO.ee,
        1: MO.my_add,
        2: MO.my_dif,
        3: MO.my_mul,
        4: MO.my_div,
        5: MO.my_pow,
        6: MO.my_sqrt,
        7: MO.shutdown
    }

    while True:
        #Переменные сбрасывают свои значения до нуля после перезапуска калькулятора или после выполнения операций, не затрагивая последний результат, если он есть
        a.value = 0
        b.value = 0

        choice = IO.get_number(int, "\nДоступные операции:\n1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление\n5. Возведение в степень\n6. Корень из числа\n7. Выход из программы\n> ", "Ошибка: Введите целое число, соответствующее номеру операции!")
        if choice in operations:
            if operations[choice] in (MO.shutdown, MO.ee):
                operations[choice]()
            else:
                if operations[choice] is MO.my_sqrt:
                    r = IO.handle_result(result.value, a)
                    result.value = operations[choice](a.value)
                    continue
                r = IO.handle_result(result.value, a, b)
                if r == "a":
                    b.value = IO.get_number(float, "Введите значение переменной b: ")
                elif r == "b":
                    a.value = IO.get_number(float, "Введите значение переменной a: ")
                else:
                    a.value = IO.get_number(float, "Введите значение переменной a: ")
                    b.value = IO.get_number(float, "Введите значение переменной b: ")
                result.value = operations[choice](a.value, b.value)
        else:
            print("Нет такой операции!")
