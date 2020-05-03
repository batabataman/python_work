import os
import csv

file_path = os.path.join("/Users", "kawabata", "Downloads", "aaa.txt")
print(file_path)

with open(file_path, "r", encoding="utf-8") as f:
    line = f.readlines()


print(type(line))        
line_ = []
for i in line:
    line_.append(i.strip())

print(line_)
#ff_list = ff.split('\n')
#print(ff_list)


aa = input("input some word:")

file_path2 = os.path.join("/Users", "kawabata", "Downloads", "bb.txt")
with open(file_path2, "w", encoding="utf-8") as f:
          f.write(aa)

csv_list = [["Top Gun", "Risky Business", "Minority Report"],
            ["Titanic", "The Reverent", "Inception"],
            ["Training Day", "Man on Fire", "Flight"]]
with open("challenge9.csv", "w", newline='') as f:
    w = csv.writer(f, delimiter=",")
    for i in csv_list:
        w.writerow(i)

csv_list2 = [["ああああ", "高円寺", "中野"],
            ["東中野", "大久保", "新宿"],
            ["阿佐ケ谷", "新高円寺", "新中野"]]
with open("challenge9_2.csv", "w", newline='',encoding='utf-8') as f:
    w = csv.writer(f, delimiter=",")
    for i in csv_list2:
        w.writerow(i)

with open("challenge9_2.csv", "r", encoding='utf-8') as f:
    r = csv.reader(f, delimiter=",")
    print(type(r))
    for i in r:
        print(i)
