def devision_2(x):
    """
    return x // 2
    :param x: int.
    """
    return x // 2

def multiply_4(y):
    """
    return y * 4
    :param y: int.
    """
    return y * 4

a = input("input number:")

try:
    a = int(a)
    a = devision_2(a)
    a = multiply_4(a)
    print(a)
except(ZeroDivisionError, ValueError):
    print("Invalid input.")
