declination = {1 : 'процент', 2 : 'процента', 3 : 'процентов'}
percent = int(input('Введите число от 0 до 20 - '))

if percent < 0 or percent > 20 :
    print('Введите положительное число от 0 до 20')
elif percent == 1:
    print(f'{percent} {declination[1]}')
elif percent <= 4 and percent != 0:
    print(f'{percent} {declination[2]}')
else:
    print(f'{percent} {declination[3]}')
