# Get the kth element in the fibonacci sequence
import timeit

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

def fibonacci(k):
    if k < 2:
        return 1
    else:
        return fibonacci(k-2) + fibonacci(k-1)

wrapped = wrapper(fibonacci, 30)
print(timeit.timeit(wrapped, number=10))

