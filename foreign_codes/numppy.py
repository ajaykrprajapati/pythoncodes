import numpy as np

def mul(x,y):
    return x*2+y*(2)
x = np.arange(0.02, 2, 0.1, None)
y = np.arange(0.02, 2, 0.1, None)
sum = 0
x_v = 0
y_v = 0
index_v = -1
for i in range(x.size):
    if i == 0:
        sum = mul(x[i],y[i])
        x_v = x[i]
        y_v = y[i]
        index_v = i+1
    else:
        c = mul(x[i],y[i])
        if sum > c:
            x_v = x[i]
            y_v = y[i]
            index_v = i+1
            sum = c
print(x_v, y_v, index_v, sum)