
def binarySearch(arr,target):
    """
    left is the left most pointer. And right is the right most pointer. 

    """
    left = 0
    right = len(arr)-1

    while (left <= right):
        mid = (left+right)//2 # Find the middle of the array

        if (arr[mid]==target):
            return mid
        elif (arr[mid]<target):
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


arr = [11,12,13,14,15,16,17]
index_of_arr = [0,1,2,3,4,5,6]

target = 11

result = binarySearch(arr,target) # Result should be index of the target

if result != -1:
    print("Element is present at index %d" %(result))
else:
    print("Element is not present in the array")
