# https://www.geeksforgeeks.org/a-product-array-puzzle/
def productArray(arr, n):  
  
    # Base case 
    if(n == 1): 
        print(0) 
        return
          
    # Allocate memory for temporary arrays left[] and right[]  
    left = [0]*n  
    right = [0]*n  
  
    # Allocate memory for the product array  
    prod = [0]*n  
  
    # Left most element of left array is always 1  
    left[0] = 1
  
    # Rightmost most element of right array is always 1  
    right[n - 1] = 1
  
    # Construct the left array  
    for i in range(1, n):  
        print("arr[i - 1]=>", arr[i - 1])
        print("left[i - 1]=>", left[i - 1])
        print("left[i]=>", left[i])
        left[i] = arr[i - 1] * left[i - 1]  
  
    # Construct the right array  
    for j in range(n-2, -1, -1):
        print("arr[j + 1]=>", arr[j + 1])
        print("right[j + 1]=>", right[j + 1])
        print("right[j]=>", right[j])  
        right[j] = arr[j + 1] * right[j + 1]  
  
    # Construct the product array using  
    # left[] and right[]  
    for i in range(n):  
        prod[i] = left[i] * right[i]  
  
    # print the constructed prod array  
    for i in range(n):  
        print(prod[i], end =' ')  
  
  
# Driver code  
arr = [10, 3, 5, 6, 2]  
n = len(arr)  
print("The product array is:")  
productArray(arr, n) 



# Python program for product array puzzle 
# with O(n) time and O(1) space. 
def solve(arr, n): 
  
    # Initialize a variable to store the  
    # total product of the array elements 
    prod = 1
    for i in arr: 
        prod *= i 
  
    # we know x / y mathematically is same  
    # as x*(y to power -1) 
    for i in arr: 
        print(int(prod//i), end =" ") 
  
# Driver Code 
arr = [10, 3, 5, 6, 2] 
n = len(arr) 
solve(arr, n) 