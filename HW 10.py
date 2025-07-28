#1.
class Soda:
    def __init__(self, additive=None):
        self.additive = str(additive) if additive is not None else ""

    def show_my_drink(self):
        if self.additive:
            print(f"Газировка и {self.additive}")
        else:
            print("Обычная газировка")

drink1 = Soda("лимон")
drink1.show_my_drink()

#2.
class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if not all(isinstance(x, (int, float)) for x in [self.a, self.b, self.c]):
            return "Нужно вводить только числа!"
        if any(x <= 0 for x in [self.a, self.b, self.c]):
            return "С отрицательными числами ничего не выйдет!"
        if (self.a + self.b <= self.c or
            self.a + self.b <= self.b or
            self.b + self.c <= self.a):
            return "Жаль, но из этого треугольник не сделать"
        return "Ура, можно построить треугольник!"

check = TriangleChecker(3, 4, 5)
print(check.is_triangle())

#3
# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = 0
#         self.set_kg(kg)
#
#     def to_pounds(self):
#         return self.__kg * 2.20462
#
#     def set_kg(self, value):
#         if not isinstance(value, (int,float)):
#             raise TypeError("Знгачение должно быть числом!")
#         if value < 0:
#             raise ValueError("Масса не может быть отрицательной")
#         self.__kg = value
#     def get_kg(self):
#         return self.__kg
#
# converter = KgToPounds(10)
# print(converter.get_kg())
# print(converter.to_pounds())
#
# converter.set_kg(5)
# print(converter.get_kg())
# print(converter.to_pounds())

#3.2
class KgToPounds:
    def __init__(self, kg):
        self.__kg = 0
        self.kg = kg

    def to_pounds(self):
        return self.__kg * 2.20462

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Значение должно быть числом")
        if value < 0:
            raise ValueError("Масса не может быть отрицательной!")
        self.__kg = value

converter = KgToPounds(10)
print(converter.kg)
print(converter.to_pounds())

converter.kg = 5
print(converter.kg)
print(converter.to_pounds())

#4
class RealString:
    def __init__(self, string):
        # Преобразуем входной аргумент в строку
        self.string = str(string)

    def __eq__(self, other):
        # Сравниваем длины для RealString или str
        if isinstance(other, (RealString, str)):
            other_len = len(other.string) if isinstance(other, RealString) else len(other)
            return len(self.string) == other_len
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, (RealString, str)):
            other_len = len(other.string) if isinstance(other, RealString) else len(other)
            return len(self.string) != other_len
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, (RealString, str)):
            other_len = len(other.string) if isinstance(other, RealString) else len(other)
            return len(self.string) < other_len
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, (RealString, str)):
            other_len = len(other.string) if isinstance(other, RealString) else len(other)
            return len(self.string) > other_len
        return NotImplemented

s1 = RealString("Apple")
s2 = RealString("Яблоко")
print(s1 < s2)
print(s1 == s2)

s3 = RealString("Hi")
print(s3 == "Привет")
print("Привет" == s3)
print(s3 > "Я")

#5
class Rectangle:
    def __init__(self, width, height):
        if not all(isinstance(x, (int, float)) for x in [width, height]):
            raise TypeError("Ширина и высота должны быть числами")
        if any(x <= 0 for x in [width, height]):
            raise ValueError("Ширина и высота должны быть положительными")
        self.width = width
        self.height = height

    def __str__(self):
        return f"Прямоугольник с шириной {self.width} и высотой {self.height}"

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    @property
    def is_square(self):
        return self.width == self.height

rect1 = Rectangle(4, 5)
print(rect1)
print(rect1.get_area())
print(rect1.get_perimeter())
print(rect1.is_square)

#6
class Person:
    def __init__(self, name, age, gender):
        if not all(isinstance(x, str) for x in [name, gender]):
            raise TypeError("Имя и пол должны быть строками")
        if not isinstance(age, (int, float)):
            raise TypeError("Возраст должен быть числом")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным")
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"Имя: {self.name}, Возраст: {self.age}, Пол: {self.gender}"

    def get_name(self):
        return self.name

    @property
    def name(self):
        return self.new_name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Новое имя должно быть строкой")
        self.new_name = new_name

    @staticmethod
    def is_adult(age):
        if not isinstance(age, (int, float)):
            raise TypeError("Возраст должен быть числом")
        return age >= 18

    @classmethod
    def create_from_string(cls, s):
        parts = s.split("-")
        if len(parts) != 3:
            raise ValueError("Строка должна иметь формат 'name-age-gender'")
        name, age_str, gender = parts
        if not all(isinstance(x, str) for x in [name, gender]):
            raise TypeError("Имя и пол должны быть строками")
        try:
            age = float(age_str)
            if age < 0:
                raise ValueError("Возраст не может быть отрицательным")
            if age.is_integer():
                age = int(age)
        except ValueError:
            raise ValueError("Возраст должен быть числом")
        return cls(name, age, gender)

person1 = Person("Alice", 25, "Female")
print(person1)
print(person1.get_name())
print(person1.name)
print(Person.is_adult(20))
print(Person.is_adult(15))

person1.name = "Bob"
print(person1)
print(person1.get_name())

person2 = Person.create_from_string("Charlie-30-Male")
print(person2)
print(person2.is_adult(person2.age))

