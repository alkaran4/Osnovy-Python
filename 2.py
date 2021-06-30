def generator_2(n):
    return (num for num in range(1, n + 1) if num % 2)

gen = generator_2(40)

print(*gen)

