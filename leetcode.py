
import itertools

# Remove vowels from string

# s = "leetcodeisacommunityforcoders"
# result = "ltcdscmmntyfrcdrs"

def removeVowels(string1):
    s = set('aeiou')
    result = ""
    for characters in string1:
        if characters not in s:
            result += characters

    return result

def removeVowels1(string1):
    vowels1 = set('aeiou')
    return ''.join(character for character in string1 if character not in vowels1)



# Running sum of 1 D Array

# nums = [1,2,3,4]
# result = [1,3,6,10]

def runningSum(nums):

    new_list = []
    new_list.append(nums[0])

    for i in range(1,len(nums)):
        new_list.append(new_list[i-1]+nums[i])

    return new_list

def runningSum1(nums):
    for i in range(1,len(nums)):
        nums[i] = nums[i] + nums[i-1]
    return nums

def runningSum2(nums):
    return list(itertools.accumulate(nums))

# Defanging an IP Address

# address = "1.1.1.1"
# result = "1[.]1[.]1[.]1"

def defang(str):
    return str.replace('.','[.]')

def defang1(str):
    return '[.]'.join(str.split('.'))

# kids with greatest number of candies
# For each kid check if there is a way to distribute extraCandies among the 
# kids such that he or she can have the greatest number of candies among them. 
# Notice that multiple kids can have the greatest number of candies.

# candies = [2,3,5,1,3]
# extraCandies = 3
# output = [true,true,true,false,true]

def extra_candy(candies,extra):

    result = []

    maxCandies = max(candies)

    for i in range(len(candies)):
        if candies[i] + extra >= maxCandies:
            result.append(True)
        else:
            result.append(False)

    return result

def extra_candy1(candies,extra):
    max_candies = max(candies)
    return [candy+extra>=max_candies for candy in candies]

# Shuffle the array

# Given array of [x1,x2,x3,y1,y2,y3] and n = 3
# return [x1,y1,x2,y2,x3,y3]

def shuffle_array(arr1,n):

    result = []

    for i in range(n):
        result.append(arr1[i])
        result.append(arr1[i+n])
    
    return result

def shuffle_array1(nums,n):
    return [num for t in zip(nums[:n],nums[n:]) for num in t]

# Richest customer wealth 

# accounts = [[1,2,3],[2,3,4]]
# result = 9 (highest)

def richest_customer(accounts):

    sum_n = []

    for i in range(0,len(accounts)):
        sum_n.append(sum(accounts[i]))

    return max(sum_n)

def richest_customer1(accounts):
    return max(map(sum,accounts))

def richest_customer2(accounts):
    maximum = float("-inf")
    for wealth in accounts:
        maximum = max(sum(wealth),maximum)
    return maximum

# Number of good pairs

# A pair of (i,j) is called good if nums[i] == nums[j] and i < j

# nums = [1,2,3,1,1,3]

# 1 has 2
# 2 has 0
# 3 has 1
# 1 has 1

# result = 4

def good_pairs(nums):

    pairs = 0
    d = {}

    for i in nums:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for num in d:
        val = d[num]
        for i in range(val):
            pairs += 1
    return pairs

print(good_pairs([1,2,3,1,1,3]))