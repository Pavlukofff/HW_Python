# Напишите код, который принимает список чисел и возвращает новый список,
# содержащий только четные числа из исходного списка. Используйте функцию
# filter и лямбда-выражение.
def get_numbers(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Неверный тип данных")
    return list(filter(lambda x: isinstance(x, int) and x % 2 == 0, numbers))
print(get_numbers([1, 2, 3, 4, 5]))

# Напишите код, который принимает список кортежей вида (имя, возраст) и
# возвращает новый список, отсортированный по возрастанию возраста.
# Используйте функцию sorted и ключ сортировки.
def sort_by_age(people):
    return sorted(people, key=lambda x: x[1])
print(sort_by_age([("pasha",22), ("sasha",55)]))

# Напишите код, который принимает список строк и возвращает новый список,
# содержащий только те строки, которые начинаются с гласной буквы. Используйте функцию filter и множество.
def filter_vowel_strings(strings):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return list(filter(lambda x: isinstance(x, str) and x and x[0].lower() in vowels, strings))
print(filter_vowel_strings(["eeghs", "fghj", "dfgudj", "odfg", "fgjdjgzfdrZwaa", "dfhgasasa"]))

# Напишите код, который принимает список чисел и возвращает новый список,
# содержащий квадраты этих чисел. Используйте функцию map и lambda.
def square_numbers(numbers):
    return list(map(lambda x: x ** 2, numbers))
print(square_numbers([1, 2, 3, 4, 5]))

# Напишите код, который принимает список слов и возвращает новый список,
# отсортированный по убыванию длины слов. Используйте функцию sorted и
# обратный порядок сортировки.
def sort_by_length(words):
    return sorted(words, key=lambda x: len(x), reverse=True)
print(sort_by_length(["собака", "кот", "кит", "муравей"]))

# Напишите код, который принимает строку и возвращает список, содержащий
# только те буквы, которые встречаются в слове “python”. Используйте функцию
# filter и оператор in.
def filter_python_letters(text):
    python_letters = {'p', 'y', 't', 'h', 'o', 'n'}
    return list(filter(lambda x: x in python_letters, text))
print(filter_python_letters("a lot of different words"))

# Напишите код, который принимает список чисел и возвращает новый список,
# содержащий эти же числа, умноженные на 10. Используйте функцию.
def multiply_by_10(numbers):
    return list(map(lambda x: x * 10, numbers))
print(multiply_by_10([1, 2, 3, 4, 5]))

# Напишите код, который принимает список слов и возвращает новый список,
# отсортированный по алфавиту. Используйте функцию sorted.
def sort_alphabetically(words):
    return sorted(words)
print(sort_alphabetically(["рыба", "ирис", "собака", "апельсин", "слон"]))

# Напишите функцию, которая принимает список строк и возвращает новый
# список, содержащий только те строки, которые являются палиндромами.
# Используйте функцию filter и сравнение строк.
def filter_palindromes(strings):
    return list(filter(lambda x: x == x[::-1], strings))
print(filter_palindromes(["наган", "роза", "шалаш"]))

# Напишите код, который принимает список слов и возвращает новый список,
# отсортированный по возрастанию количества гласных букв в словах.
# Используйте функцию sorted и ключ сортировки.
# def count_vowels(word):
#     vowels = {'a', 'e', 'i', 'o', 'u'}
#     return sum(c.lower() in vowels for c in word)
# def sort_by_vowel_count(words):
#     return sorted(words, key=count_vowels)

def sort_by_vowel_count(words):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return sorted(words, key=lambda x: sum(c.lower() in vowels for c in x))
print(sort_by_vowel_count(["rdathdfsgs", "awerrt", "yuujfguu", "opasfka", "dfhdfghfgdo"]))

# Напишите код, который принимает список строк и возвращает новый список,
# содержащий эти же строки в верхнем регистре. Используйте функцию map и
# встроенный метод строк upper.
def to_uppercase(strings):
    return list(map(str.upper, strings))
print(to_uppercase(["awfa", "dsfgsdf", "sdfgdfsger", "asdrfsg", "sdfgsdfg"]))

# Напишите код, который принимает список строк и возвращает новый список,
# содержащий эти же строки с добавленным префиксом “Hello”. Используйте
# функцию map и конкатенацию строк.
def hello_prefix(strings):
    return list(map(lambda x: "Hello" + x, strings))
print(hello_prefix(["hello", "world"]))

# Напишите код, который принимает список слов и возвращает новый список,
# отсортированный по возрастанию количества букв “a” в словах. Используйте
# функцию sorted и ключ сортировки.
def sort_by_a_count(words):
    return sorted(words, key=lambda x: x.lower().count('а'))
print(sort_by_a_count(["ара", "рама", "роза", "алалала"]))

# Напишите код, который принимает список слов и возвращает новый список,
# отсортированный по возрастанию количества уникальных букв в словах.
# Используйте функцию sorted и ключ сортировки.
# def count_unique_letters(word):
#     return len(set(word.lower()))
# def sort_by_unique_letters(words):
#     return sorted(words, key=count_unique_letters)

def sort_by_unique_letters(words):
    return sorted(words, key=lambda x: len(set(x.lower())))
print(sort_by_unique_letters(["лошадь", "крыша", "машина", "собака"]))

# Напишите декоратор retry_five, который повторяет вызов декорируемой
# функции 5 раз.
def retry_five(func):
    def wrapper(*args, **kwargs):
        result = None
        for _ in range(5):
            result = func(*args, **kwargs)
        return result
    return wrapper

@retry_five
def try_it():
    print("Тест...")
try_it()