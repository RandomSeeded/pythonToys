# Get the kth element in the fibonacci sequence
def fibonacci(k):
    performed = {}
    def inner(k):
        if k < 2:
            return 1

        a = performed[k-2] if k-2 in performed else inner(k-2)
        b = performed[k-1] if k-1 in performed else inner(k-1)
        result = a+b
        performed[k] = result
        return result

    inner(k)

import timeit
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

wrapped = wrapper(fibonacci, 30)
print(timeit.timeit(wrapped, number=10))
