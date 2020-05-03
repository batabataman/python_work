a = input("input number:")

def square(a):
    """
    Returns a ** 3
    :param a: int
    """
    return a ** 2

try:
    a = int(a)
    a = square(a)
    print(a)
except ValueError:
    print("Invalid input.")
