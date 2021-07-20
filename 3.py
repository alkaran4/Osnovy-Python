class Cell:

    def __init__(self, size):
        self.size = size

    def __str__(self):
        return self.size * '*'

    def __add__(self, other):
        return (self.size + other.size) * '*'

    def __sub__(self, other):
        return (self.size - other.size) * '*'

    def __mul__(self, other):
        return (self.size * other.size) * '*'

    def __floordiv__(self, other):
        return (self.size // other.size) * '*'

    def make_order(self, number):
        print(((number * '*' + '\n') * (self.size // number)) + self.size % number * '*')

a = Cell(45)
print(a)
a.make_order(8)
