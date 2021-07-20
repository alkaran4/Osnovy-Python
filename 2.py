class Clothes:

    def __init__(self, size):
        self.size = size

    @property
    def cloth(self):
        pass

    def __add__(self, other):
        return self.size + other.size


class Coat(Clothes):

    @property
    def cloth(self):
        return self.size / 6.5 + 0.5



class Suit(Clothes):

    @property
    def cloth(self):
        return 2*self.size + 0.3


ct = Coat(42)
st = Suit(50)
print(ct + st)


