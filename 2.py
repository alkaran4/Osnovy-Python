uneven_numbers = []
for i in range(1000):
    if i % 2 != 0:
        uneven_numbers.append(i ** 3)

sum_number_7 = 0
for number in uneven_numbers:
    sum_digit = 0
    for digit in str(number):
        sum_digit += int(digit)
    if sum_digit % 7 == 0:
        sum_number_7 += number

print('список кубов нечетных чисел', uneven_numbers)
print('сумма чисел, сумма цифр которых делится на 7', sum_number_7)
print('\n')

for idx in range(len(uneven_numbers)):
    uneven_numbers[idx] += 17

sum_number_17 = 0
for number in uneven_numbers:
    sum_digit = 0
    for digit in str(number):
        sum_digit += int(digit)
    if sum_digit % 7 == 0:
        sum_number_17 += number

print('список кубов нечетных чисел + 17', uneven_numbers)
print('сумма чисел, сумма цифр которых делится на 7', sum_number_17)
