

list1 = [
    [-1, 3],
    [0,512],
    [-2000,2],
]

class Matrix:
    def __init__(self, m: list[list[int | float]]):
        self.__m = m
        self.__width = len(m[0])
        self.__height = len(m)

    def __str__(self) -> str:
        text = ""

        max_elem = max([max(row) for row in self.__m])
        max_elem = len(str(max_elem)) + 2

        for row in self.__m:
            text += "| "
            for element in row:
                text += f"{element:>{max_elem}}"
            text += " |\n"
        return text

# Сложение матриц (только одинаковых размерностей)
    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Объект не является матрицей")
        if self.__width !=other.__width or self.__height != other.__height:
            raise ValueError("Размерность матриц не совпадает")

        new_matrix = []
        for i in range(self.__height):
            new_row = []
            for j in range(self.__width):
                new_row.append(self.__m[i][j] + other.__m[i][j])
            new_matrix.append(new_row)

        return Matrix(new_matrix)

m1=Matrix(list1)
m2=Matrix(list1)

print(m1 + m2)