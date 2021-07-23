class OwnExcept(Exception):

    def __init__(self, text):
        self.text = text


answer, dict_1 = 0, []

while answer != 'stop':
    try:
        answer = input('Введите число - ')
        if not answer.isdigit():
            raise OwnExcept('Это не число')
    except OwnExcept as err:
        print(err)
    else:
        dict_1.append(answer)

print(dict_1)
