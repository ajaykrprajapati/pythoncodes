lst = [1, 2, 3, 3, 4]
n = len(lst) -1 #nottice difference here from duplicate to missing ele ques
from functools import reduce
x = sum(lst)
tot =  (n*(n+1))/2
mis =  x-tot
print(int(mis))









lst = [1, 2, 3, 4, 4]

x = lst[0]
y = 1

for i in range(1, len(lst)):
    x ^=lst[i]

for i in range(2, len(lst)): #nottice difference here from duplicate to missing ele ques
    y ^=i

print(x^y)