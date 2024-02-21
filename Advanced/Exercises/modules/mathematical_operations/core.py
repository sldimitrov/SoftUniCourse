
def divide(a: float, b: float) -> float:
    try:
        result = a / b
    except ZeroDivisionError:
        print("You cannot divide by zero!")
    else:
        return result


def multiply(a: float, b: float) -> float:
    return a * b


def subtract(a: float, b: float) -> float:
    return a - b


def addition(a: float, b: float) -> float:
    return a + b


def raising(a: float, b: float) -> float:
    return a ** b
