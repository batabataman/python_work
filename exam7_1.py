shows = {"G. Bluth II": "A. Development",
         "Barney": "HIMYM",
         "Dennis": "Always Sunny"}

if "Barney" in shows:
    print("equals")
    
for show in shows:
    print(show)
    print(shows[show])
    if "Barney" == show:
        print("key equals")


print("==============")
tv = ["GOT", "Narcos", "Vice"]
i = 0
for i,new in enumerate(tv):
    new = tv[i]
    new = new.upper()
    print(new)
    tv[i] = new

print(tv)

print("==============")

tv = ["GOT", "Narcos", "Vice"]
coms = ["Arrested Development", "friends", "Always Sunny"]
all_shows = []
tv2 = tv
print(tv2)
for show in tv:
    show = show.upper()
    all_shows.append(show)

for show in coms:
    show = show.upper()
    all_shows.append(show)

print(all_shows)
tv[0] = "Ramone"
print(tv)
print(tv2)
print(all_shows)

print("==============")
for i in range(1, 11):
    print(i)
    

x = 10
while x > 0:
    print('{}!'.format(x))
    x -= 1
print(" Happy New Year!")

qs = ["What is your name?:",
      "What is your fav. color?:",
      "What is your quest?:"]

n = 0
while True:
    print(n)
    print("Type q to quit")
    a = input(qs[n])
    if a == "q":
        break
    n = (n + 1) % 3

print(0 % 3)
print(1 % 3)
print(2 % 3)
