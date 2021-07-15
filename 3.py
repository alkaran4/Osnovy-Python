def logger(func):
    def wrapper(*args, **kwarg):
        result = func(*args, **kwarg)
        print({i: type(i) for i in args})
        return result

    return wrapper


@logger
def my_sum(a, b):
    return a + b


print(my_sum(10, 5))
