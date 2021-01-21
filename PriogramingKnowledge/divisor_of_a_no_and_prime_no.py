
#24 [1,2,3,4,6,8,12,24]
from math import sqrt
x1 = [ i for i in range(1, int(sqrt(24)+1)) if 24%i ==0]
x2 = [ 24//i for i in range(1, int(sqrt(24)+1)) if 24%i ==0]
x1.extend(x2)

#prime
O(root n)
def prime_check(n):
    if n==0 or n==1:
        return False
    if n==2 or n==3:
        return True
    if n%2==0 or n%3==0:
        return False
    for i in range(5, int(sqrt(n))+1):
        if n%i==0 or n%(1+2)==0:
            return False
    return True