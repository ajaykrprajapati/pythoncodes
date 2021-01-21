#left shift: (Adding zero to end)
# shifting m.s.b value by 1 left
# eg:
# N=22
0 0 0 1 0 1 1 0
0 0 1 0 1 1 0 0 (shifting first zero to last)
#this is multiple of 2
22<< i means 22*(2,pow(i))

#Right shift:(Adding zero to start)
22>> i means 22/(2,pow(i))

# Q1) Finding ith set bit 
# +++++++++++++++++++++++++++++++++++++++++
# given: n = 5(101)
# i(pos) = 1 result= False
# i(pos) = 2 result= True
# link: https://www.youtube.com/watch?v=IO2D1g2QP6E&list=PL2q4fbVm1Ik7ip1VkWwe5U_CEb93vw6Iu&index=3&ab_channel=CodeNCode
Sol: Left shift
f = 1(000000001)
f << i 
n and f == 0 if bit is not set else set

# Q2 find the no. of set bit in n
# given : n=5(101) return 2
# https://www.youtube.com/watch?v=_o7QBzM33J0&list=PL2q4fbVm1Ik7ip1VkWwe5U_CEb93vw6Iu&index=4&ab_channel=CodeNCode
Sol: Right shift
approach 1)
n=8
f = 1
count = 0
while n>0:
    if (n & f) != 0:
        count +=1
    n = n>>1
print(count)

approach 2)
n = 8
count = 0
while n>0:
    count +=1
    n = (n & n-1)
print(count)


# Q) if n is power of 2
# https://www.youtube.com/watch?v=zSxsECATphs&list=PL2q4fbVm1Ik7ip1VkWwe5U_CEb93vw6Iu&index=7&ab_channel=CodeNCode
n=15
count = 0
while n>0:
    count +=1
    n = (n & (n-1))
print(True) if count==1 else print(False)






# XOR:
# +++++++++++++
1^1 =0, 0^0 =0
Identity element = 0
0^n = n
n^n

x = [1,1,2,2,3,4,4]
from functools import reduce
res = reduce(lambda x,y:x^y, x)
res
