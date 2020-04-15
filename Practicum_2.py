def g(a, b, *args, name = "Default", **kwargs):
    print(a, b, args, name, kwargs)


g(1, 2, 3, 4, 5, c=6, d=10)