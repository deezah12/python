import functools
import time


def decorate(func):
    @functools.wraps(func)
    def wrap(*args, **kwargs):
        print("i am a before decorator ")
        print(func(*args, **kwargs))
        print("i am after decorator")

    return wrap


@decorate
def hello(name):
    return f"hello {name} world"


def performance_count(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func = f(*args, **kwargs)
        end = time.perf_counter()
        print(f"the function {f.__name__} took {end - start} to run")
        return func

    return wrapper


@performance_count
@decorate
def add(x, y):
    """"
    adds two numbers
    """
    return x + y


# how @decorate works underground
# hello = decorate(hello)
hello("dee")
add(2, 4)
print(add.__name__)
print(add.__doc__)


def multiply(a, b):
    return a * b


multiply_by_5 = functools.partial(multiply, 5)
multiply_by_6 = functools.partial(multiply, 6)

print(multiply_by_5(6))
print(multiply_by_6(6))
