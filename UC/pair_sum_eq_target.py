# https://www.geeksforgeeks.org/count-pairs-with-given-sum/

Sign In
Home
Courses
Hire With Us
Algorithmskeyboard_arrow_down
Data Structureskeyboard_arrow_down
Languageskeyboard_arrow_down
Interview Cornerkeyboard_arrow_down
GATEkeyboard_arrow_down
CS Subjectskeyboard_arrow_down
Studentkeyboard_arrow_down
GBlog
Puzzles
What's New ?
▲
Count pairs with given sum
Given an array A[] and a number x, check for pair in A[] with sum as x
Majority Element
Find the Number Occurring Odd Number of Times
Largest Sum Contiguous Subarray
Maximum Subarray Sum using Divide and Conquer algorithm
Maximum Sum SubArray using Divide and Conquer | Set 2
Sum of maximum of all subarrays | Divide and Conquer
Finding sum of digits of a number until sum becomes single digit
Program for Sum of the digits of a given number
Compute sum of digits in all numbers from 1 to n
Count possible ways to construct buildings
Maximum profit by buying and selling a share at most twice
Maximum profit by buying and selling a share at most k times
Stock Buy Sell to Maximize Profit
Maximum difference between two elements such that larger element appears after the smaller number
Given an array arr[], find the maximum j – i such that arr[j] > arr[i]
Sliding Window Maximum (Maximum of all subarrays of size k)
Sliding Window Maximum (Maximum of all subarrays of size k) using stack in O(n) time
Next Greater Element
Next greater element in same order as input
Next Greater Frequency Element
Number of NGEs to the right
Maximum product of indexes of next greater on left and right
The Celebrity Problem
Write a program to reverse an array or string
Program for array rotation
Find the smallest and second smallest elements in an array
Arrays in Java

Count pairs with given sum
Last Updated: 04-06-2020
Given an array of integers, and a number ‘sum’, find the number of pairs of integers in the array whose sum is equal to ‘sum’.

Examples:

Input  :  arr[] = {1, 5, 7, -1}, 
          sum = 6
Output :  2
Pairs with sum 6 are (1, 5) and (7, -1)

Input  :  arr[] = {1, 5, 7, -1, 5}, 
          sum = 6
Output :  3
Pairs with sum 6 are (1, 5), (7, -1) &
                     (1, 5)         

Input  :  arr[] = {1, 1, 1, 1}, 
          sum = 2
Output :  6
There are 3! pairs with sum 2.

Input  :  arr[] = {10, 12, 10, 15, -1, 7, 6, 
                   5, 4, 2, 1, 1, 1}, 
          sum = 11
Output :  9
Expected time complexity O(n)

Recommended: Please solve it on “PRACTICE” first, before moving on to the solution.
A simple solution is be traverse each element and check if there’s another number in the array which can be added to it to give sum.
filter_none
edit
play_arrow

brightness_4
# Python3 implementation of simple method 
# to find count of pairs with given sum. 
  
# Returns number of pairs in arr[0..n-1]  
# with sum equal to 'sum' 
def getPairsCount(arr, n, sum): 
      
    count = 0 # Initialize result 
  
    # Consider all possible pairs 
    # and check their sums 
    for i in range(0, n): 
        for j in range(i + 1, n): 
            if arr[i] + arr[j] == sum: 
                count += 1
      
    return count 
  
# Driver function  
arr = [1, 5, 7, -1, 5] 
n = len(arr) 
sum = 6
print("Count of pairs is", 
      getPairsCount(arr, n, sum)) 
  
# This code is contributed by Smitha Dinesh Semwal 

Output :

ADVERTISING



Count of pairs is 3
Time Complexity : O(n2)
Auxiliary Space : O(1)

 
A better solution is possible in O(n) time.

Below is the Algorithm.

Create a map to store frequency of each number in the array. (Single traversal is required)
In the next traversal, for every element check if it can be combined with any other element (other than itself!) to give the desired sum. Increment the counter accordingly.
After completion of second traversal, we’d have twice the required value stored in counter because every pair is counted two times. Hence divide count by 2 and return.
Below is the implementation of above idea :
filter_none
edit
play_arrow

brightness_4
# Python 3 implementation of simple method 
# to find count of pairs with given sum. 
import sys 
  
# Returns number of pairs in arr[0..n-1]  
# with sum equal to 'sum' 
def getPairsCount(arr, n, sum): 
      
    m = [0] * 1000
      
    # Store counts of all elements in map m 
    for i in range(0, n): 
        m[arr[i]] += 1
  
    twice_count = 0
  
    # Iterate through each element and increment 
    # the count (Notice that every pair is  
    # counted twice) 
    for i in range(0, n): 
      
        twice_count += m[sum - arr[i]]  
  
        # if (arr[i], arr[i]) pair satisfies the 
        # condition, then we need to ensure that 
        # the count is  decreased by one such  
        # that the (arr[i], arr[i]) pair is not 
        # considered 
        if (sum - arr[i] == arr[i]): 
            twice_count -= 1
      
    # return the half of twice_count 
    return int(twice_count / 2)  
  
# Driver function  
arr = [1, 5, 7, -1, 5]  
n = len(arr) 
sum = 6
  
print("Count of pairs is", getPairsCount(arr, 
                                     n, sum)) 