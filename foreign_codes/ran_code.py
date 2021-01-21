import numpy as np

def rowsum(matrix):
    """
    :param matrix (list): A list of lists where each inner list represents a row.
    :returns: (list) A list containing the sum of each row.
    """
    mat = np.array(matrix)
    return mat.sum(axis=1)

print(rowsum([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) 




#Display top3 students:
import numpy as np
marks = [98,34,55,11,100]
students = ["A","C","B","E","D"]
m = np.array(marks)
s = np.array(students)
s[m.argsort()[::-1]][:3].tolist()



import numpy_indexed as npi
students = [["Ana Stevens", "1a", 5], ["Mark Stevens", "1a", 4], ["Jon Jones", "1a", 2], ["Bob Kent", "1b", 4]]
s = np.array(students)
npi.group_by(students[:,1:2]).mean(students)




def find_unique_numbers(numbers):
    return None

print(find_unique_numbers([1, 2, 1, 3]))




from collections import defaultdict 
def find_unique_numbers(numbers):

    d = defaultdict(int) 
    for i in numbers:
        d[i] += 1
    res = []
    for k, v in d.items():
        if v==1:
            res.append(k)
    return res
print(find_unique_numbers([1, 2, 1, 3]))




from enum import Enum

class Side(Enum):
    none = 0
    left = 1
    right = 2

class ChainLink:

    def __init__(self):
        self._left = None
        self._right = None

    def append(self, link):
        if self._right is not None: raise Exception('Link already connected!')
        self._right = link
        link._left = self

    def longer_side(self):
        return None

left = ChainLink()
middle = ChainLink()
right = ChainLink()
left.append(middle)
middle.append(right)
print(left.longer_side() == Side.right)



class MovingTotal:
    def __init__(self):   
        self.lst = [] 
    
    def find3Numbers(self,A, arr_size, sum): 
        for i in range(0, arr_size-1): 
            s = set() 
            curr_sum = sum - A[i] 
            c=0
            for j in range(i + 1, arr_size): 
                if (curr_sum - A[j]) in s: 
                    return True
                if c<2:
                    c+=1
                else:
                    break
                s.add(A[j]) 
        return False

    def append(self, numbers):
        """
        :param numbers: (list) The list of numbers.
        """
        self.lst.extend(numbers)

    def contains(self, total):
        """
        :param total: (int) The total to check for.
        :returns: (bool) If MovingTotal contains the total.
        """
        return self.find3Numbers(self.lst,len(self.lst), total)
        
    
    
if __name__ == "__main__":
    movingtotal = MovingTotal()
    movingtotal.append([1, 2, 3])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    movingtotal.append([4])
    print(movingtotal.contains(7))





    from typing import Dict, Tuple, Callable, Iterable

import numpy

def model_quadratic(model_parameters: dict):
    a = model_parameters['a']
    b = model_parameters['b']
    c = model_parameters['c']
    return 1.75 + (a - 0.5) ** 2 + (b - 0.75) ** 2 + (c - 0.25) ** 2

class Problem:
    @staticmethod
    def grid_search(search_space: Dict[str, Iterable],
                    scoring_func: Callable[[Dict[str, float]], float]) -> Tuple[float, Dict[str, float]]:
        
        x = search_space['a']
        y = search_space['b']
        z = search_space['c']
        print(x)
        print(y)
        print(z)
        print(x.size())
        for i in range(x.size):
            if i == 0:
                sum = scoring_func({"a":x[i],"b":y[i],"c":z[i]})
                print("sum1==>", sum)
                x_v = x[i]
                y_v = y[i]
                z_v = z[i]
            else:
                c = scoring_func({"a":x[i],"b":y[i],"c":z[i]})
                if sum > c:
                    x_v = x[i]
                    y_v = y[i]
                    z_v = z[i]
                    sum = c
        return sum, {'a': x_v, 'b': y_v, 'c': z_v}


print(Problem.grid_search({
    'a': numpy.arange(0.0, 1.0, 0.05),
    'b': numpy.arange(0.0, 1.0, 0.05),
    'c': numpy.arange(0.0, 1.0, 0.05),
}, model_quadratic))