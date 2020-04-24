"""Считать с клавиатуры отдельными операторами:
- заголовок страницы (например, Hello);
- цвет заголовка первого уровня (например, blue);
- цвет текста абзаца (например, red);
- текст заголовка первого уровня (например, Title 1);
- текст статьи (например, Article text).

Использовать только латинские символы.
Используя декораторы, сформировать текст html-страницы для публикации статьи."""
# Считывание через input()
# Hello
# blue
# red
# Title 1
# Article text

from functools import wraps

title = input()
color_h1 = input()
color_text = input()
text_h1 = input()
art_text = input()

# Этот вариант более сжатый, но, который выбрал я, на мой взгляд более изящный
# def head_part_1(func):
#     @wraps(func)
#     def inner(text):
#         print('<html>')
#         print('<head>')
#         func(text)
#     return inner
#
#
# def head_part_2(func):
#     @wraps(func)
#     def inner(text_1, text_2):
#         func(text_1, text_2)
#         print('</head>')
#     return inner
#
#
# def body_part(func):
#     @wraps(func)
#     def inner(text_1, text_2):
#         print('<body>')
#         func(text_1, text_2)
#         print('</body>')
#         print('</html>')
#     return inner
#
#
# @head_part_1
# def head_part(text):
#     print('<title>' + text + '</title>')
#
#
# @head_part_2
# def head_part_i(text_1, text_2):
#     print('<style>' + 'h1{color:' + text_1 + '}'
#           + 'p{color:' + text_2 + '}' + '</style>')
#
#
# @body_part
# def body_part_1(text_1, text_2):
#     print('<h1>' + text_1 + '</h1>')
#     print('<p>' + text_2 + '</p>')
#
#
# head_part(title)
# head_part_i(color_h1, color_text)
# body_part_1(text_h1, art_text)


def make_html(fn):
    def inner(*args, **kwargs):
        print("<html>")
        fn(*args, **kwargs)
        print("</html>")
    return inner


def make_head(fn):
    def inner(*args, **kwargs):
        print("<head>")
        fn(*args, **kwargs)
        print("</head>")
    return inner


def make_title(fn):
    def inner(*args, **kwargs):
        print("<title>")
        fn(*args, **kwargs)
        print("</title>")
    return inner


def make_style(fn):
    def inner(*args, **kwargs):
        print("<style>")
        fn(*args, **kwargs)
        print("</style>")
    return inner


def make_body(fn):
    def inner(*args, **kwargs):
        print("<body>")
        fn(*args, **kwargs)
        print("</body>")
    return inner


def make_par(fn):
    def inner(*args, **kwargs):
        print("<p>")
        fn(*args, **kwargs)
        print("</p>")
    return inner


def make_h1(fn):
    def inner(*args, **kwargs):
        print("<h1>")
        fn(*args, **kwargs)
        print("</h1>")
    return inner


@make_html
def page(text_1, text_2, text_3, text_4, text_5):
    @make_head
    def head_part(text1, text2, text3):
        @make_title
        def head_part_1(x):
            print(x)

        @make_style
        def head_part_2(x,y):
            print('h1{color:' + x + '}' +
                  '\np{color:' + y + '}')

        head_part_1(text1)
        head_part_2(text2, text3)

    @make_body
    def body_part(text4, text5):
        @make_h1
        def body_part_1(x):
            print(x)

        @make_par
        def body_part_2(y):
            print(y)

        body_part_1(text4)
        body_part_2(text5)

    head_part(text_1, text_2, text_3)
    body_part(text_4, text_5)


page(title, color_h1, color_text, text_h1, art_text)

