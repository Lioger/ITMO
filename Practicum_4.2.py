"""Считать одной строкой произвольное количество пар элементов "Название книги Число экземпляров",
второй строкой название алгоритма хеширования md5:
Aibolit 66 Barmaley 67
md5

Создать 2 класса:
1-й преобразует строку вида 'Aibolit 66 Babmaley 67', где название книги уникально, в словарь.
2-й осуществляет хеширования названия книги алгоритмом md5.
Вывести отдельными операторами вывода:
- элементы словаря, отсортированные по возрастанию ключа, например:
Aibolit 66
Barmaley 67
- результаты хеширования в виде пар названия алгоритма и результатов хеширования ключей, отсортированных по возрастанию,
представленных в шестнадцатеричном виде, сведенных в одну строку через пробел вида
md5 c47.... md5 5d....' (без пробелов в начале и конце строки)."""
import hashlib


class Preob(object):
    dict_1 = {}

    def __init__(self, str_x):
        self.list_1 = str_x.split()
        for i in range(0, len(self.list_1), 2):
            self.dict_1.update({self.list_1[i]: int(self.list_1[i + 1])})

    def get_dict(self):
        for i, j in sorted(self.dict_1.items()):
            print(i, j)


class Hashing(Preob):
    def __init__(self, method):
        self.method = method
        super(Preob, self).__init__()

    def hashin(self):
        for key in sorted(self.dict_1):
            print("md5", hashlib.md5(key.encode()).hexdigest(), end=" ")


input_str = input('Введите название книги и число экземпляров (Пример: "Aybolit 60"): ')
input_method = input('Введите метод шифрования (Пример: "md5"): ')
Preob(input_str).get_dict()
Hashing(input_method).hashin()
