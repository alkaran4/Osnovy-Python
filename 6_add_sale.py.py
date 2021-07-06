from sys import argv

with open("bakery.csv", 'r', encoding='utf-8') as f:
    prices = f.read().split(',')

enter = [int(item) for item in argv[1:]]

print(enter)
if not enter:
    print(prices)
elif len(enter) == 1:
    result = [int(item) for item in prices[enter[0] - 1:]]
    print(f'результат: {result}')
elif len(enter) == 2:
    result= [int(item) for item in prices[enter[0] - 1:enter[1]]]
    print(f'результат: {result}')


