"""Считать несколько имен людей одной строкой, записанных латиницей, через пробел, например:
«Anna Maria Peter».
Вывести их одной строкой в порядке возрастания «Anna Maria Peter».
Вывести их одной строкой в порядке убывания «Peter Maria Anna»."""

lst = input().split()
print(*sorted(lst))
print(*sorted(lst, reverse=True))

# Сначала я сделал задание менее элегантно, но тоже верно
# lst = input().split()
# sorted_list = sorted(lst)
# print(' '.join(sorted_list))
# reversed_list = reversed(sorted_list)
# print(' '.join(reversed_list))
