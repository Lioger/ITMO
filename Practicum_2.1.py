"""Считать отдельными операторами целочисленные ширину и высоту прямоугольника. Создать функцию (def), принимающую
в качестве параметров ширину и высоту фигуры и название функции, которую необходимо выполнить. Имя вложенной функции
передавать явным образом (например: (a,b,name='perim')).
Внутри функции создать две вложенные функции (def) по подсчету площади и периметра фигуры. Вывести одной строкой
через пробел площадь и периметр, разделенные пробелом (например, '20 18')."""


def geometry(a, b, name='perim'):
    def perim(a, b):
        return 2*(a+b)

    def plosh(a, b):
        return a*b

    if name == 'perim':
        return perim(a, b)
    elif name == 'plosh':
        return plosh(a, b)


a = int(input())
b = int(input())
x1 = geometry(a, b, 'plosh')
x2 = geometry(a, b, 'perim')
print(x1, x2)

# Можно использовать такой вариант, но он не соответствует тому уровню, какой дали к моменту этой лабы
# def func(x, y, name):
#     def plosh(x, y):
#         return x * y
#
#     def perim(x, y):
#         return (x + y) * 2
#
#     return locals()[name](x, y)
#
#
# x = int(input())
# y = int(input())
# print(func(x, y, "plosh"), func(x, y, "perim"))
