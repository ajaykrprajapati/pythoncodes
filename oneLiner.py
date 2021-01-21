#if-else:

# True_stament if condition else False_statment


print(" This side true statment") if 10 > 15 else print("Else print hua hai bhai")

# For loop

x = [i for i in range(1, 100, 2)]



########################################################
##lambda

minus = lambda x, y : x-y
print(minus(5,3))


########################################################

#map,filter and reduce

# [opration(i*3) iterator(for i in range(10)) condition (if x==10)]

##  map(func, list)
mylist = [1, 2, 3, 4, 5, 6, 7]
square = list(map(lambda x: x*x, mylist))

filterr = list(filter(lambda x : x>3, mylist))

from functools import reduce
reducee = reduce(lambda x,y: x+y, mylist)

#list comprehension
x = [ i for i in range(100) if i%3 == 0]




########################################################

#dict comphrension
dict1 = { i:f"item {i}" for i in range(10) if i%2==0}
# reverse dict key val
dict2 = { value:key for key, value in dict1.items()}





########################################################

# https://www.hackerrank.com/challenges/python-lists/forum

lst = [4,5,6,7,8]
x = " insert 1 2"
w = x.split()
# int_conv = tuple(map(int, w[1:]))
int_conv = w[1:]
print(int_conv)
print(type(w[0]))
cmd  = w[0]+"("+",".join(int_conv)+")"
print(cmd)
eval("lst."+cmd)
########################################################



in_n_out = "Bling GlibN"
ow, sw = in_n_out.split()
print("ow :", ow, " sw:", sw)
res = ""
for word in ow:
    indx = sw.lower().find(word.lower())
    print("indx: ",indx)
    res = res + str(indx)
    print("res1: ", res)
    if sw[indx].isupper() and word.isupper():
        k = "O"
    elif sw[indx].islower() and word.islower():
        k = "O"
    elif sw[indx].isupper() and word.islower():
        k = "U"
    else:
        k = "L"
    res +=k
    print("res2: ", res)
print(res)


input_matrix= [[38,40,9],[23,40,25],[45,34,33]]
mat_len = len(input_matrix)
# print(mat_len)
lst = []
for i in range(mat_len):
    for j in range(mat_len):
        lst.append(int(input_matrix[i][j]))
# print(lst)
x = lst[:mat_len]
lst.sort(reverse=True)
z = lst[:mat_len]
# print(x, z)
c= 0
for key in z:
    if key in x:
        x.remove(key)
    else:
        c+=1
print(c)


#Sorting:
# ++++++++++++++++++++
mylist = [10,7,4,18,6,9,3]
print(mylist)
x = sorted(mylist)
y = sorted(mylist, reverse=True)
print(x,y)
mylist.sort(reverse=True)
print(mylist)
mylist.sort()
print(mylist)


my_list = [3,1,5,2]
k = {v:k for k,v in enumerate(my_list)}
k


#Ques: return list of index which adds up to target t
# ++++++++++++++++++++++++++++++++
# https://leetcode.com/problems/two-sum/submissions/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        k = [(v,k) for k,v in enumerate(nums)]
        k.sort()
        begin = 0
        end = len(k)-1
        while begin<end:
            _sum = k[begin][0] + k[end][0]
            if _sum == target:
                res = sorted([k[begin][1], k[end][1]])
                return(res)    
            elif _sum > target:
                end -= 1
            else:
                begin +=1
  