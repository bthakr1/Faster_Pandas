
"""

|  |__|  |  /  _]| |      /  ] /   \ |   |   |  /  _]    |  ||  ||  |
|  |  |  | /  [_ | |     /  / |     || _   _ | /  [_     |  ||  ||  |
|  |  |  ||    _]| |___ /  /  |  O  ||  \_/  ||    _]    |__||__||__|
|  `  '  ||   [_ |     /   \_ |     ||   |   ||   [_      __  __  __ 
 \      / |     ||     \     ||     ||   |   ||     |    |  ||  ||  |
  \_/\_/  |_____||_____|\____| \___/ |___|___||_____|    |__||__||__|
                                                                     

"""


# Problem Statement : Given an array of integers of size N, find maximum sum of K consecutive elements.
import sys

INT_MIN = -sys.maxsize - 1

def bruteForce(arr,n,k):

    """
    arr : Array 
    n : number of elements in the array 
    k : number of elements needed to be added
    """
    # Initialize result

    max_sum = INT_MIN

    for i in range(n - k + 1):
        current_sum = 0
        for j in range(k):
            current_sum = current_sum + arr[i + j]
        
        max_sum = max(current_sum,max_sum)
    
    return max_sum

arr = [80,-50,90,100]
n = len(arr)
k = 3

print(bruteForce(arr,n,k))