import sys
def get_second_largest_element(arr, arr_size):
    '''
    Returns second largest element if exist or else -1.

            Parameters:
                    arr (list): sample list
                    arr_size (int): size of array

            Returns:
                    second (int): second largest element if exist or else -1
    '''
    #There should be atleast two elements
    if (arr_size < 2):
        return -1    
    
    const = int("9"*1024)*-1
    first = second = const
    for i in range(arr_size):
        # If current element is smaller than first then update both first and second 
        if (arr[i] > first):
            second = first
            first = arr[i]
         
        # If arr[i] is in between first and second then update second 
        elif (arr[i] > second and arr[i] != first):
            second = arr[i]
     
    return -1 if (second == const) else second
 
 
# Driver program to test above function 
arr = list(map(int,input("\nEnter the numbers : ").strip().split()))
arr_len = len(arr)
get_second_largest_element(arr, arr_len)