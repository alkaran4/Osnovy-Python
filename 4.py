peoples = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for words in peoples:
    word = words.split()
    print(f' Привет {word.pop().capitalize()}!')
