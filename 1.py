matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matrix_2 = [[11, 12, 13], [14, 15, 16], [17, 18, 19]]


class Matrix:

    def __init__(self, list):
        self.list = list

    def __str__(self):
        return '\n'.join(map(str, self.list))

    def __add__(self, other):
        list_1 = []
        for i in range(len(self.list)):
            list_1.append([])
            for x in range(len(self.list)):
                list_1[i].append(self.list[i][x] + other.list[i][x])
        return '\n'.join(map(str, list_1))


mt1 = Matrix(matrix_1)

mt2 = Matrix(matrix_2)

print(mt1 + mt2)