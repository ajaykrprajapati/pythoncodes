from collections import defaultdict 
def nth_most_rare(elements, n):
    """
    :param elements: (list) List of integers.
    :param n: (int) The n-th element function should return.
    :returns: (int) The n-th most rare element in the elements list.
    """
    d = defaultdict(int) 
    for i in elements:
        d[i] += 1
    res = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
    c = 0
    for key in res.keys():
        c+=1
        if c == n:
            return key
        

print(nth_most_rare([5, 4, 2, 1, 5, 4, 2, 5, 4, 3, 5, 4, 5], 2))