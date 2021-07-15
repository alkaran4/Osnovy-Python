class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}, занимает должность {self.position}'

    def get_total_income(self):
        return f'{self.name} {self.surname}, имеет общий доход {self._income["wage"] + self._income["bonus"]}'


Mark = Position("Марк", "Цукерберг", "Директор", 100000, 15000)

print(Mark.get_full_name())
print(Mark.get_total_income())
