def ft_filter(func, arr):
    """ Do func for every arr elements """
    try:
        print(type(func))
        func(arr)
    except:
        pass
    [func(i) for i in arr]


def f(x):
    print(x+1)

ft_filter(f, 2)