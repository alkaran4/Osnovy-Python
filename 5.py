prices = [57.8, 46.51, 97, 45.57, 189.97, 23, 76.66]

for price in prices:
    rub_kop = str(price).split('.')
    if len(rub_kop) == 1:
        print(f'{int(rub_kop[0])} руб 00 коп')
    else:
        print(f'{rub_kop[0]} руб {int(rub_kop[1]):02d} коп')

# 2я часть задачи
print(id(prices))
prices.sort()
print(prices)
print(id(prices))

# 3я часть задачи
prices_reverse = sorted(prices.copy(), reverse = True)
print(prices_reverse)
print(id(prices_reverse))

# 4я часть задачи
for top_5_price in range(5):
    print(prices_reverse[top_5_price])
