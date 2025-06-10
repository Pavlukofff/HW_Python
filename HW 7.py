# Напишите функцию make_sentence, которая принимает один именованный
# аргумент words, который должен быть списком строк, и возвращает строку,
# составленную из элементов списка, разделенных пробелами и
# заканчивающуюся точкой. Если аргумент words не указан, то по умолчанию
# используется список ["This", "is", "a", "sentence"].
def make_sentence(*, words=["This", "is", "a", "sentence"]):
    return " ".join(words) + "."
print(make_sentence(words=["ggdfgh", "et"]))

# Напишите функцию sum_of_squares, которая принимает произвольное
# количество позиционных аргументов, которые должны быть числами, и
# возвращает сумму их квадратов. Если функции не передано ни одного
# аргумента, она должна вернуть 0.
def sum_of_squares(*args):
    return sum(x * x for x in args)
print(sum_of_squares(1,2,3,4))

# Напишите функцию greet, которая принимает два именованных аргумента:
# name и language. Аргумент name должен быть строкой, а аргумент language
# должен быть одним из трех возможных значений: "en", "ru" или "fr".
# Функция должна возвращать приветствие на выбранном языке.
# Если аргумент language не указан, то по умолчанию используется "en".
def greet(*, name, language="en"):
    greetings = {
        "en": "Hello",
        "ru": "Привет",
        "fr": "Bonjour"
    }
    return f"{greetings[language]}, {name}!"
print(greet(name="Pasha", language="fr"))

# Напишите функцию print_info, которая принимает произвольное
# количество именованных аргументов (**kwargs) и выводит их в формате
# "key: value" по одной паре на строку. Напоминаю, что kwargs в функции
# будет словарем. Если функции не передано ни одного аргумента, она должна
# вывести "No info given.".
def print_info(**kwargs):
    if kwargs:
        for key, value in kwargs.items():
            print(f"{key}: {value}")
    else:
        print("No info given.")
print_info(name="Alex", age=25, city="Amsterdam")

# Напишите функцию print_table, которая принимает произвольное
# количество именованных аргументов в виде пар ключ-значение и выводит их
# в виде таблицы с двумя столбцами: "Key" и "Value". Если функции не
# передано ни одного аргумента, она должна вывести "No data given.".
def print_table(**kwargs):
    if not kwargs:
        print("No data given.")
        return
    items = [(key, str(value)) for key, value in kwargs.items()]
    key_width = max(len("Key"), max(len(key) for key, _ in items))
    value_width = max(len("Value"), max(len(value) for _, value in items))
    print(f"{'Key':<{key_width}} | {'Value':<{value_width}}")
    print(f"{'-' * key_width}-|-{'-' * value_width}")
    for key, value in items:
        print(f"{key:<{key_width}} | {value:<{value_width}}")
print_table(name="Bob", age=30, city="Amsterdam")

# Напишите функцию calculate, которая принимает произвольное количество
# позиционных аргументов, которые должны быть числами, и один
# именованный аргумент operation, который должен быть одним из четырех
# возможных значений: "+", "-", "*" или "/".
# Функция должна возвращать результат выполнения указанной операции над
# всеми числами в порядке их передачи.
# Если функции не передано ни одного позиционного аргумента, она должна
# вернуть 0.
# Если аргумент operation не указан, то по умолчанию используется "+".
def calculate(*args, operation="+"):
    if not args:
        return 0
    if operation == "+":
        return sum(args)
    if operation == "-":
        result = args[0]
        result -= sum(args[1:])
        return result
    if operation == "*":
        result = 1
        for i in args:
            result *= i
        return result
    if operation == "/":
        result = args[0]
        for i in args[1:]:
            try:
                result /= i
            except ZeroDivisionError:
                print("division by zero")
        return result
print(calculate(1, 2, 3, operation="/"))

# Напишите функцию print_triangle, которая принимает один именованный
# аргумент height, который должен быть положительным целым числом, и
# выводит равнобедренный треугольник из символов "*" с заданной высотой.
# Если аргумент height не указан, то по умолчанию используется число 5.
def print_triangle(*, height=5):
    for i in range(1, height + 1):
        print(" " * (height - i) + "*" * (2 * i - 1))
print_triangle(height=10)

# Напишите функцию create_post, которая создает пост для блога,
# основываясь на переданных параметрах. Обязательными параметрами
# являются: заголовок, содержимое и автор. Необязательным параметром
# является категория. Если она не была передана, то по умолчанию будет
# текущая значение “general”. Функция должна возвращать словарь поста.
def create_post(*, title, content, author, category="general"):
    return {
        "title": title,
        "content": content,
        "author": author,
        "category": category
    }
print(create_post(title="one", content="some", author="she", category="general"))

# Напишите функцию create_product, которая создает товар для интернет
# магазина, основываясь на переданных параметрах. Обязательными
# параметрами являются: имя, цена и категория. Необязательным параметром
# является рейтинг. Если он не был передан параметр, то по умолчанию будет
# 0. Функция должна возвращать словарь товара.
def create_product(*, name, price, category, rating=0):
    return {
        "name": name,
        "price": price,
        "category": category,
        "rating": rating
    }
print(create_product(name="one", price=100, category="phone", rating=2))

# Напишите функцию create_student, которая создает словарь студента
# для учебного заведения, основываясь на переданных параметрах.
# Обязательными параметрами являются: имя, фамилия, отчество и группа.
# Также дополнительными параметрами могут быть: дата поступления в виде
# строки «19.10.2023», средний бал, семестр обучения, номер телефона, адрес.
# Функция должна возвращать словарь студента только с переданными
# данными, если некоторые данные не были переданы, то их не должно быть
# в словаре.
def create_student(*, name, surname, patronymic, group, admission_date=None, average_grade=None, semester=None,
                   phone_number=None, address=None):
    if not all(isinstance(x, str) for x in [name, surname, patronymic, group]):
        raise TypeError("name, surname, patronymic, and group must be strings")
    student = {
        "name": name,
        "surname": surname,
        "patronymic": patronymic,
        "group": group
    }
    if admission_date is not None:
        student["admission_date"] = admission_date
    if average_grade is not None:
        student["average_grade"] = average_grade
    if semester is not None:
        student["semester"] = semester
    if phone_number is not None:
        student["phone_number"] = phone_number
    if address is not None:
        student["address"] = address
    return student
print(create_student(name='pasha', surname='pavlukov', patronymic='sergeevich', group='py64', semester='1'))