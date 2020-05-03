import os
import csv

a=os.path.join("User", "kawabata", "test.txt")
print(a)

st = open("st.txt", "w", encoding="UTF-8")
st.write("Pythonからこんにちは")
st.close()

with open("st2.txt", 'w', encoding="utf-8") as f:
    f.write("aaaa")
    f.write("ああああ")

my_list = []
with open("st2.txt", 'r', encoding="utf-8") as f:
    my_list.append(f.read())

print(my_list)


with open("st.csv", "w", encoding="utf-8") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["one", "two", "three"])
    w.writerow(["four", "five", "six"])

with open("st.csv", "r", encoding="utf-8") as f:
    r = csv.reader(f, delimiter=",")
    for i in r:
        print(i)
        print(",".join(i))


