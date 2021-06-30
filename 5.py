src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
data = sorted(set(src), key=lambda d: src.index(d))
print(data)
print(set(src))
