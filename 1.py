def generator_1(n):
    for i in range(1, n + 1, 2):
        yield i

gen = generator_1(160)


print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
