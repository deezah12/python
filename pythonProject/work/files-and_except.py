def add(a: float, b: float) -> float | None:
    try:
        return a / b
    except ZeroDivisionError:
        print("can't divide by zero")
        return None
    except TypeError:
        print("Type error")


print(add(1, 0))
