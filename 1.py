import re


def email_parse(data):
    parse = re.compile(r'(\w+)\@(\S+)')
    dict = {'username': parse.findall(data)[0][0], 'domain' : parse.findall(data)[0][1]}
    return dict

print(str(email_parse('someone@geekbrains.ru')))

