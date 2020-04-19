"""Создайте класс, осуществляющий подсчет и изменение числа книг. Названия книг, их количество считываются
одной строкой вида 'Boogeyman 66 Battleground 50', число книг - произвольное.
В классе должен быть реализован конструктор, деструктор, методы просмотра числа, взятия и возвращения книг.
Реализовать вывод начальных значений, взятие по 1 книге, возвращение по 1 книге с выводом текущего числа
после вызова каждого из методов, меняющих значение книг.
Типичный ответ одной строкой: 'Boogeyman 66 65 66 Battleground 50 49 50'."""
list_1 = input().split()


class Books(object):
    def __init__(self, listik):
        self.list_final = listik
        self.boog_count = int(self.list_final[1])
        self.batt_count = int(self.list_final[3])
        self.score = 2

    def __del__(self):
        pass

    def boog_counter(self):
        return self.boog_count

    def batt_counter(self):
        return self.batt_count

    def books_take(self):
        self.boog_count -= 1
        self.batt_count -= 1
        self.list_final.insert(self.score, self.boog_count)
        self.list_final.append(self.batt_count)
        self.score += 1

    def books_return(self):
        self.boog_count += 1
        self.batt_count += 1
        self.list_final.insert(self.score, self.boog_count)
        self.list_final.append(self.batt_count)
        self.score += 1


book = Books(list_1)
book.books_take()
book.books_return()
print(*book.list_final)
