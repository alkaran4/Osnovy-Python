from requests import get, utils

def currency_rates(arg):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    content = content.split('</Value>')
    date = content[0][(content[0].index('Date=')) + 6:(content[0].index('Date=')) + 16]
    # 6 - количество символов в 'Date=' + 1; 16 - количество символов в дате
    for i in content:
        if arg.upper() in i:
            n = 8
            # 8 - количество цифр в валюте с курсом больше 100 рублей. Не самое удачное решение, до другого не допер
            if not i[-n].isdigit():
                n -= 1
            currency = i[-n:].split(',')
            return (f'Курс {arg.upper()} на {date} составляет {float(".".join(currency))} рублей.')


print(currency_rates("eur"))
print(currency_rates("usd"))
print(currency_rates("usd"))



