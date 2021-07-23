class Zero:

    @staticmethod
    def tryer(numerator, divisor):
        try:
            print(f'Результат деления - {numerator / divisor}')
        except ZeroDivisionError:
            print('На ноль делить нельзя')

Zero.tryer(25, 0)
Zero.tryer(25, 5)
