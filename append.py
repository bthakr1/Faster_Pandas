nums = [1,2,3,4]

# First solution

n = len(nums)
sum = 0

for i in range(0,n):
    sum +=  nums[i]

print("sum of array : ", sum)

n = len(nums)

print("sum of array ", n*(n+1)/2)