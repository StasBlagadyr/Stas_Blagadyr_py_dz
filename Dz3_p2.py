#Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
#в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
def thesaurus(*names):
    out_dict = dict()
    for name in names:
        out_dict.setdefault(name[0], [])
        out_dict[name[0]].append(name)
    return out_dict

print(thesaurus("Иван", "Мария", "Петр", "Илья", "Stas", "Dina"))