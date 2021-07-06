with open("name.csv", "r", encoding='utf-8') as f:
    n = f.read().split('\n')
print(n)
with open("hobby.csv", "r", encoding='utf-8') as f:
    h = f.read().split('\n')

for name, hobby in zip(n, h):
    result = {name : hobby}
    # print(result)
