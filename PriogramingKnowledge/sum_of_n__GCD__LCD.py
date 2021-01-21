#euclid algo
# T.C = o(log(min(a,b)))
def GCD(x,y):
    if x == 0:
        return y
    GCD(y%x,x)

# product = lcm * gcd
def LCM(x,y):
    product = x*y
    gcd = GCD(x,y)
    return product//gcd

t = int(input())
while(t):
    n = int(input())
    print((n*(n-1))//2)
    t -=1