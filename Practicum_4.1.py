"""Создайте класс, осуществляющий подсчет и изменение числа книг. Названия книг, их количество считываются
одной строкой вида 'Boogeyman 66 Battleground 50', число книг - произвольное.
В классе должен быть реализован конструктор, деструктор, методы просмотра числа, взятия и возвращения книг.
Реализовать вывод начальных значений, взятие по 1 книге, возвращение по 1 книге с выводом текущего числа
после вызова каждого из методов, меняющих значение книг.
Типичный ответ одной строкой: 'Boogeyman 66 65 66 Battleground 50 49 50'."""


class Books(object, list_1=input().split()):
    def __init__(self):
        self.lib = []
        for i in list_1:
            if i.isdigit():
                self.lib.append([int(i)])
            else:
                self.lib.append([i])


    def __del__(self):
        del Books

    def books_count(self):
        pass

    def books_take(self):
        pass

    def books_return(self):
        pass


book = Books.books_count(*list_1)
