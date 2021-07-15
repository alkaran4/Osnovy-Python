class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки c помощью {self.title}')


class Pen(Stationery):

    def draw(self):
        print(f'Отрисовка карандашом')

class Pencil(Stationery):

    def draw(self):
        print(f'Отрисовка ручкой')

class Handle(Stationery):

    def draw(self):
        print(f'Отрисовка маркером')


a = Pen('a')
b = Pencil('b')
c = Handle('c')
x = Stationery('x')


a.draw()
b.draw()
c.draw()
x.draw()
