
doramas = ["ウォーキング・デッド", "アントラージュ", "ザ・ソプラノズ", "ヴァンパイア・ダイアリーズ"]

for dorama in doramas:
    print(dorama)

for i in range(25, 51):
    print(i)

for i, dorama in enumerate(doramas):
    print(i)
    print(dorama)

correct_numbers = [1, 2, 3]
while True:
    a = input("input some word:")
    if a == "q":
        break
    else:
       try:
           a_ = int(a)
           if a_ in correct_numbers:
               print("correct")
           else:
               print("please input correct number")
       except ValueError:
           print("please input number or \'q\'")
       print("test")


nums1 = [8, 19, 148, 4]
nums2 = [9, 1, 33, 83]
all_nums = []

for num1 in nums1:
    for num2 in nums2:
        num_result = num1 * num2
        all_nums.append(num_result)

for i, num in enumerate(all_nums):
    print(all_nums[i])
    print(num)


numbers = [11, 32, 33, 15, 1]

while True:
    answer = input("Guess a number or type q to quit.")
    if answer == "q":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("please type a number or q to quit.")
    if answer in numbers:
        print("You guessed correctly!")
    else:
        print("You guessed incorrectly!")
