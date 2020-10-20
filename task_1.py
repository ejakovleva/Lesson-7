class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        y_1 = [[] for _ in self.matrix]
        try:
            for a, b in enumerate(self.matrix):
                for c, d in enumerate(self.matrix[a]):
                    y_1[a].append(self.matrix[a][c] + other.matrix[a][c])
            return Matrix(y_1)
        except (IndexError, TypeError):
            return Matrix("Размерность матриц должна быть одинаковой!")

    def __str__(self):
        y_2 = []
        for i, j in enumerate(self.matrix):
            y_2.append([f'{a}' for a in self.matrix[i]])
        y_3 = []
        for i, j in enumerate(y_2):
            y_3.append(' '.join(y_2[i]))
        return '\n'.join(y_3)


matrix_1 = Matrix([[1, 2, 3], [3, 4, 5], [5, 6, 7]])
matrix_2 = Matrix([[3, 4, 5], [5, 6, 7], [8, 9, 10]])
matrix_3 = Matrix([[10, 12, 15], [13, 14, 1], [20, 21, 18]])
matrix_4 = Matrix([[10, 12, 1], [8, 13, 14], [9, 20, 21]])
print(matrix_1 + matrix_2 + matrix_3 + matrix_4)




