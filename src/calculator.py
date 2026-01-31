def _validate_numbers(*args):
    for value in args:
        if not isinstance(value, (int, float)):
            raise ValueError("All inputs must be numeric")


def fun1(x, y):
    """
    Adds two numbers.
    """
    _validate_numbers(x, y)
    return x + y


def fun2(x, y):
    """
    Subtracts y from x.
    """
    _validate_numbers(x, y)
    return x - y


def fun3(x, y):
    """
    Multiplies two numbers.
    """
    _validate_numbers(x, y)
    return x * y


def fun4(x, y):
    """
    Combines results of fun1, fun2, and fun3.
    """
    add_result = fun1(x, y)
    sub_result = fun2(x, y)
    mul_result = fun3(x, y)

    return add_result + sub_result + mul_result
