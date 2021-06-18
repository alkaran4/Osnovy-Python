first_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for index in first_list:
    idx = first_list.index(index)
    if index.isdigit():
        first_list[idx] = f'{int(index):02d}'
    elif not index.isdigit() and not index.isalpha():
        first_list[idx] = f'{int(index):+03d}'


sentance = ' '.join(first_list)

print(first_list)
print(sentance)



