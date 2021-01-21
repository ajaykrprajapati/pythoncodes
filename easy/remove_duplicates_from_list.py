
#method 1
lst = ["5","3","2","3","1","5","3"]
# out: ["2","1"]
int_lst = list(map(lambda x:int(x), lst))
print(list(set(int_lst)))




#mthod 2
lst = ["5","3","2","3","1","5","3"]
# out: ["2","1"]
int_lst = list(map(lambda x:int(x), lst))
int_lst = list(dict.fromkeys(lst))
print(int_lst)





#mthod: Remove duplicates from list using list comprehension
my_list = [1,2,2,3,1,4,5,1,2,6]
my_finallist = []
[my_finallist.append(n) for n in my_list if n not in my_finallist] 
print(my_finallist)



#mthod 4 : Remove duplicates from list using Numpy unique() method.
import numpy as np
my_list = [1,2,2,3,1,4,5,1,2,6]
print(np.unique(my_list).tolist())





#methos using Pd
import pandas as pd

my_list = [1,2,2,3,1,4,5,1,2,6]
myFinalList = pd.unique(my_list).tolist()
print(myFinalList)





# Remove duplicates using enumerate() and list comprehension
dup_list = ["1","2","2","3","1","4","5","1","2","6"]
dup_list = list(map(lambda x:int(x), my_list))
no_dup_list = [i for j, i in enumerate(dup_list) if i not in dup_list[:j]] 
