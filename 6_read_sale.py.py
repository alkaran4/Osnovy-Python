from sys import argv

enter = [int(item) for item in argv[1:]]
en = str(enter[0])

with open("bakery.csv", 'a', encoding='utf-8') as f:
    prices = f.write(f'{en} ,')
