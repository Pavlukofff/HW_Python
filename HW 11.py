import copy
from typing import Union, List


class Matrix:
    def __init__(self, m: List[List[Union[int, float]]]):
        if not m or not m[0]:
            raise ValueError("Матрица не может быть пустой!")
        if not all(isinstance(elem, (int, float)) for row in m for elem in row):
            raise TypeError("Все элементы должны быть числами!")
        width = len(m[0])
        if not all(len(row) == width for row in m):
            raise ValueError("Матрица должна быть прямоугольной!")
        self.__m = copy.deepcopy(m)
        self.__width = width
        self.__height = len(m)

    @property
    def matrix(self):
        return copy.deepcopy(self.__m)

    def __str__(self) -> str:
        if not self.__m:
            return "[]"
        max_len = max(len(str(elem)) for row in self.__m for elem in row)
        max_len += 2
        text = ""
        for row in self.__m:
            text +="| "
            for elem in row:
                text += f"{elem:>{max_len}}"
            text += " |\n"
        return text

# Сложение матриц (только одинаковых размерностей)
    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Объект не является матрицей")
        if self.__width !=other.__width or self.__height != other.__height:
            raise ValueError("Размерность матриц не совпадает")
        new_matrix = [[self.__m[i][j] + other.matrix[i][j] for j in range(self.__width)] for i in range(self.__height)]
        return Matrix(new_matrix)

    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Обьект не является мтарицей!")
        if self.__width != other.__width or self.__height != other.__height:
            raise ValueError("Размерности матриц не совпалдают!")
        new_matrix = [[self.__m[i][j] - other.matrix[i][j] for j in range(self.__width)] for i in range(self.__height)]
        return Matrix(new_matrix)

    def __mul__(self, scalar: Union[int, float]):
        if not isinstance(scalar, (int, float)):
            raise TypeError("Множжитель должен быть числом!")
        new_matrix = [[self.__m[i][j] * scalar for j in range(self.__width)] for i in range(self.__height)]
        return Matrix(new_matrix)

    def transpose(self):
        new_matrix = [[self.__m[j][i] for j in range(self.__height)] for i in range(self.__width)]
        return Matrix(new_matrix)

    @classmethod
    def identity(cls, m: int, n: int):
        if m <= 0 or n <= 0:
            raise ValueError("Размеры матрицы должны быть положительными!")
        matrix = [[1 if i == j else 0 for j in range(n)] for i in range(m)]
        return cls(matrix)

    @classmethod
    def zero(cls, m: int, n: int):
        if m <= 0 or n <= 0:
            raise ValueError("Размеры матрицы должны быть положительными!")
        matrix = [[0 for j in range(n)] for i in range(m)]
        return cls(matrix)

    @classmethod
    def diagonal(cls, values: List[Union[int, float]]):
        if not values:
            raise ValueError("Список значений не может быть пукстым!")
        if not all(isinstance(x, (int, float)) for x in values):
            raise TypeError("Все элементы списка должны быть числами!")
        n = len(values)
        matrix = [[values[i] if i == j else 0 for j in range(n)] for i in range(n)]
        return cls(matrix)

    def shape(self) -> tuple:
        return self.__height, self.__width

    def size(self) -> int:
        return self.__height * self.__width

    def sum(self) -> Union[int, float]:
        return sum(elem for row in self.__m for elem in row)

    def zero_negatives(self):
        new_matrix = [[max(0, elem) for elem in row] for row in self.__m]
        return Matrix(new_matrix)

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False
        if self.shape() != other.shape():
            return False
        return all(self.__m[i][j] == other.matrix[i][j] for i in range(self.__height) for j in range(self.__width))



m1 = Matrix([[-1, 3], [0, 512], [-2000, 2]])
m2 = Matrix([[-1, 3], [0, 512], [-2000, 2]])
print(m1)
print("m1 + m2:")
print(m1 + m2)
print("m1 - m2:")
print(m1 - m2)
print("m1 * 2:")
print(m1 * 2)
print("m1 transposed:")
print(m1.transpose())
print("Identity 3x3:")
print(Matrix.identity(3, 3))
print("Zero 2x3:")
print(Matrix.zero(2, 3))
print("Diagonal [1, 2, 3]:")
print(Matrix.diagonal([1, 2, 3]))
print("Shape of m1:", m1.shape())
print("Size of m1:", m1.size())
print("Sum of m1:", m1.sum())
print("m1 with negatives zeroed:")
print(m1.zero_negatives())
print("m1 == m2:", m1 == m2)
print("m1 == m1 + m2:", m1 == m1 + m2)


