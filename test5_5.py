
def to_float(x):
    """
    return cast int to float.
    :param x: int.
    :return: convaert str to float
    """
    try:
        x = float(x)
    except ValueError:
        print("Invalid input.")
    return x

a = input("input number.")
a = to_float(a)
print(a)

    

