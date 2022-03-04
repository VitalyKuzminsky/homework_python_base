from typing import List


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        line_len = len(matrix[0])
        for line in matrix:
            if len(line) != line_len:
                raise ValueError('fail initialization matrix')
        self.matrix = matrix

    def __str__(self):
        matrix = []
        for line in self.matrix:
            matrix.append(f'| {" ".join(map(str, line))} |')
        return '\n'.join(matrix)

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError('the matrices are not equal')
        matrix = []
        for line_1, line_2 in zip(self.matrix, other.matrix):
            matrix.append(list(map(sum, zip(line_1, line_2))))
        return Matrix(matrix)


if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    #first_matrix = Matrix([[1, 2, 1], [3, 4, 1], [5, 6, 1]])  #проверка на сложение матриц большего размера
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
    #second_matrix = Matrix([[6, 5, 1], [4, 3, 1], [2, 1, 1]])  #проверка на сложение матриц большего размера
    print(first_matrix)
    #print(second_matrix)  # проверка печати второй матрицы
    """
    | 1 2 |
    | 3 4 |
    | 5 6 |
    """
    print()  # добавил принт разделить первую матрицу и сумму матриц
    print(first_matrix + second_matrix)
    """
    | 7 7 |
    | 7 7 |
    | 7 7 |
    """
    fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])
    """
    Traceback (most recent call last):
      ...
    ValueError: fail initialization matrix
    """
