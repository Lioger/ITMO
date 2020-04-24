"""Считать с клавиатуры полный адрес англоязычной html страницы.
С использованием urlparse получить из адреса кортеж значений.
Вывести текст всех заголовков уровня h1 одной строкой через пробел без дополнительных символов вначале и конце строки.
Примечание. Если внутри тегов h1 содержатся ссылки, то нужно выводить вместе со ссылками."""
# http://en.ifmo.ru/en/contacts/Contacts.htm строка для input
# !!!ВНИМАНИЕ!!! Этот файл по непонятной для меня причине не принимается
# системой ИТМО, если у вас есть почему, напишите, пожалуйста
import urllib.request
import urllib.parse
from urllib.parse import urlparse

url = input()
output_list = []
html_file = urllib.request.urlopen(url).read().decode('utf-8')
f = open('fake_page.html', 'w')
with 
f.writelines(html_file)

for line in html_file.split():
    if "<h1>" in line:
        output_list.append(line[4:-5:])
print(tuple(urlparse(url)))
print(*output_list)

# Этот вариант принимается системой ИТМО
# import urllib.request
# import urllib.parse
# from urllib.parse import urlparse
# import os
# url = input()
# output_list = []
# html_file = urllib.request.urlopen(url).read().decode('utf-8')
# f = open('fake_page.html', 'w')
# for line in html_file:
#     f.write(line)
# f = open('fake_page.html', 'r')
# for line in f.readlines():
#     if "<h1>" in line:
#         line_strip = line.strip()
#         output_list.append(line_strip[4:-5:])
# f.close()
# os.remove('fake_page.html')
# print(tuple(urlparse(url)))
# print(*output_list)
