import math
import random
import statistics
import keyword

a=math.pow(2,3)
print(a)
print(int(a))

b = random.randint(0,100)
print(b)

#mean
nums = [1, 5, 33, 12, 46, 33, 2]
c = statistics.mean(nums)
print(c)

#median
c = statistics.median(nums)
print(c)

#mode
c = statistics.mode(nums)
print(c)

print(keyword.iskeyword("for"))
print(keyword.iskeyword("f"))

