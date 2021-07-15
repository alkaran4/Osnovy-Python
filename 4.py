import os

size_of = [100, 1000, 10000, 50000, 100000]
count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
count_5 = 0

for r in os.scandir('some_data'):
    if r.stat().st_size < size_of[0]:
        count_1 += 1
    if size_of[0] < r.stat().st_size < size_of[1]:
        count_2 += 1
    if size_of[1] < r.stat().st_size < size_of[2]:
        count_3 += 1
    if size_of[2] < r.stat().st_size < size_of[3]:
        count_4 += 1
    if size_of[1] < r.stat().st_size < size_of[4]:
        count_5 += 1

dict_1 = {size_of[0]:count_1, size_of[1]:count_2, size_of[2]:count_3, size_of[3]:count_4, size_of[4]:count_5}
print(dict_1)