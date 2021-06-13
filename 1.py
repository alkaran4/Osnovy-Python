second = int(input('Введите количество секунд - '))

if second < 0:
    print('Время не может принимать отрицательное знчение')
elif second < 60:
    print(f'{second} секунд')
elif second < 3600:
    minut = second // 60
    second = second % 60
    print(f'{minut} минут, {second} секунд')
elif second < 86400:
    hour = second // 3600
    minut = (second % 3600) // 60
    second = second % 60
    print(f'{hour} часов, {minut} минут, {second} секунд')
elif second < 2592000:
    day = second // 86400
    hour = (second % 86400) // 3600
    minut = ((second % 86400) % 3600) // 60
    second = second % 60
    print(f' {day} дней, {hour} часов, {minut} минут, {second} секунд')
elif second < 31536000:
    month = second // 2592000
    day = (second % 2592000) // 86400
    hour = ((second % 2592000) % 86400) // 3600
    minut = (((second % 2592000) % 86400) % 3600) // 60
    second = second % 60
    print(f'{month} месяца, {day} дней, {hour} часов, {minut} минут, {second} секунд')
else:
    year = second // 31536000
    month = (second % 31536000) // 2592000
    day = ((second % 31536000) % 2592000) // 86400
    hour = (((second % 31536000) % 2592000) % 86400) // 3600
    minut = ((((second % 31536000) % 2592000) % 86400) % 3600) // 60
    second = second % 60
    print(f'{year} лет, {month} месяца, {day} дней, {hour} часов, {minut} минут, {second} секунд')
