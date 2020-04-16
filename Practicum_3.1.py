"""Ввести с клавиатуры строку латиницей (1-3 слова). Зашифровать ее с использованием гарантированных алгоритмов шифрования.
Сформировать словарь, где в качестве ключа используется название гарантированного алгоритма шифрования, а в качестве
значения - результат шифрования в шестнадцатеричном представлении.
Итог вывести отдельными операторами вывода в виде пар ключа и значения, отсортированных по возрастанию ключа:
md5 sha1 sha224 sha256 sha384 sha512"""

import hashlib as hs
str_1 = str(input())
dict_1 = {'md5': hs.md5(str_1.encode()).hexdigest(), 'sha1': hs.sha1(str_1.encode()).hexdigest(), 'sha224': hs.sha224(str_1.encode()).hexdigest(),
          'sha256': hs.sha256(str_1.encode()).hexdigest(), 'sha384': hs.sha384(str_1.encode()).hexdigest(), 'sha512': hs.sha512(str_1.encode()).hexdigest()}
h_1 = sorted(dict_1.items())
for key, val in h_1:
    print(key, val)