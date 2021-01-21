#https://www.geeksforgeeks.org/python-sort-values-first-list-using-second-list/?ref=rp

# Method Using numpy:
# +++++++++++++++++++++++++
import numpy as np
list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]

# out: ['a', 'd', 'h', 'b', 'c', 'e', 'i', 'f', 'g']
list1 = np.array(list1)
list2 = np.array(list2)
list1[list2.argsort()].tolist()





# Method Using zip:
# +++++++++++++++++++++++++
list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]
[x for _,x in sorted(zip(list2, list1))]








#By using Dictionary, list comprehension, lambda function

#Sort values of first list using second list
list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]

sort_dict = [x for x,_ in sorted({list1[i]:list2[i] for i in range(len(list2))}.items(), key = lambda item:item[1])]
print(sort_dict)