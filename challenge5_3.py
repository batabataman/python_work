
my_dict = dict()

my_dict = {"tall":180, "calor":"red"}

print(my_dict)

my_dict = {"comic":"dragon ball"}

print(my_dict)

input_key = input("キーを入力してください:")

if input_key in my_dict:
    print(my_dict[input_key])
else:
    print("does not exit key")
    
