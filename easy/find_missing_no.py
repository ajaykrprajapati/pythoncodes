lst = [1, 2, 3, 5]
n = len(lst) + 1
from functools import reduce
x = sum(lst)
tot =  (n*(n+1))/2
mis = tot - x
print(int(mis))

# O(n)
# O(1)



#Method 2

lst = [1, 2, 3, 5]

x = lst[0]
y = 1

for i in range(1, len(lst)):
    x ^=lst[i]

for i in range(2, len(lst)+2):
    y ^=i

print(x^y)
