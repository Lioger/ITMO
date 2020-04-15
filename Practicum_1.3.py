"""Считать единой строкой без пробелов набор целых чисел (28745623873465386),
удалить все дубликаты, вывести отдельными операторами вывода в порядке возрастания
и в порядке убывания в виде кортежей целых чисел (2, 3, 4, 5, 6, 7, 8) и (8, 7, 6, 5, 4, 3, 2)."""

# Возможно, есть более изящный способ, но я его не увидел

lst = list(input())
for i in range(len(lst)):
    lst[i] = int(lst[i])
lst_cleared = set(lst)
tuple_1 = tuple(sorted(lst_cleared))
tuple_2 = tuple(sorted(lst_cleared, reverse=True))
print(tuple_1)
print(tuple_2)