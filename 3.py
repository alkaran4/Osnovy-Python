def thesaurus(*args):
    dict_name_letter = {}
    for name in args:
        if not name[0] in dict_name_letter:
            dict_name_letter.setdefault(name[0], [name])
        else:
            dict_name_letter[name[0]].append(name)
    return dict_name_letter

print(thesaurus('Илья', 'Валерия', 'Инна', 'Оксана', 'Валентина', 'Игорь', 'Ольга', 'Владислав', 'Олег'))
