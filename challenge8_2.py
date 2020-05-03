import cubed

a = input("数字を入力してください:")

try:
    a = int(a)
    print(cubed.cube(a))
except ValueError:
    print("数字を入力してください")
