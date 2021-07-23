class ComplexNumber:

    def __init__(self, list):
        self.list = list

    def __add__(self, other):
        print(self.list[0] + other.list[0], self.list[1] + other.list[1])

    def __mul__(self, other):
        print((self.list[0] * other.list[0] - self.list[1] * other.list[1]), (self.list[0] * other.list[1] + self.list[1] * other.list[0]))


n1 = ComplexNumber([1, 2])
n2 = ComplexNumber([3, 4])
print(n1 + n2)
print(n1 * n2)
