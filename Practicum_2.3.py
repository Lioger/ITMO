"""Считать отдельными операторами целочисленные ширину и высоту прямоугольника, создать список из лямбда функций
подсчета площади и периметра фигуры. Вывести первым оператором индекс лямбда функции подсчета площади и ее
результат (например:0 20); вторым оператором индекс лямбда функции подсчета периметра и ее результат
(например:1 18); вывести третьим оператором список полученным значений (например: [20, 18]); вывести
четвертым оператором итоговые значения, сведенные в одну строк через пробел (например: '20 18')."""

x = int(input())
y = int(input())


def func(x, y):
    lst = [lambda x, y: x*y, lambda x, y: 2*(x+y)]
    for i, arg in enumerate(lst):
        print(i, arg(x, y))

    print([lst[0](x, y), lst[1](x, y)])
    print(lst[0](x, y), lst[1](x, y))


func(x, y)
