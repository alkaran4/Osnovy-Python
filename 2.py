dict_one_to_ten = {'Zero' : 'Ноль',
                   'One': 'Один',
                   'Two': 'Два',
                   'Three': 'Три',
                   'Four': 'Четыре',
                   'Five': 'Пять',
                   'Six': 'Шесть',
                   'Seven' : 'Семь',
                   'Eight' : 'Восемь',
                   'Nine' : 'Девять',
                    'Ten' : 'Десять'}

def translate(digit):
    print(dict_one_to_ten.get(digit.title()))

translate('five')
