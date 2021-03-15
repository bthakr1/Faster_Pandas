
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

# Jewels and Stones

# jewels = "aA"
# stones = "aAAbbbb"

# result = 3

# how many of the stones are in jewels

def find_jewels(jewels,stones):
    counter = 0
    jewels = set(jewels)
    for stone in stones:
        if stone in jewels:
            counter += 1
    return counter

def find_jewels1(jewels,stones):
    return sum(i in jewels for i in stones)

def find_jewels2(jewels,stones):
    result = 0
    for i in set(jewels):
        result += stones.count(i)
    return result


# count items matching a rule

# Input: items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"
# Output: 1
# Explanation: There is only one item matching the given rule, which is ["computer","silver","lenovo"].

def match_items(items,ruleKey,ruleValue):
    ruleKeys = ["type","color","name"]
    ruleKeyIndex = ruleKeys.index(ruleKey)

    
    c = 0

    for i in range(len(items)):
        if items[i][ruleKeyIndex] == ruleValue:
            c += 1
    
    return c

def match_items1(items,ruleKey,ruleValue):
    return sum((ruleKey,ruleValue) in (('type',t),('color',c),('name',n)) for t,c,n in items)

# Design parking system

# Input
# ["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
# [[1, 1, 0], [1], [2], [3], [1]]
# Output
# [null, true, true, false, false]

class ParkingSystem:

    def __init__(self,big,medium,small):
        self.vehicle = [big,medium,small]

    def addCar(self,carType):

        if carType == 1:
            if self.vehicle[0] > 0:
                self.vehicle[0] -= 1
                return True

        elif carType == 2:
            if self.vehicle[1] > 0:
                self.vehicle[1] -= 1
                return True

        elif carType == 3:
            if self.vehicle[2] > 0:
                self.vehicle -= 1
                return True

        return False

# how many numbers are smaller than the current number

# Input : nums = [8,1,2,2,3]

# output = [4,0,1,1,3]

def smaller_numbers(nums):

    return [len([k for k in nums if k <n]) for n in nums]

    
# Number of steps to reduce a number to zero

# Input num = 14
# Output 6
# 14 / 2 = 7 :1
# 7-1 = 6 :2
# 6 / 2 = 3 :3
# 3 -1 = 2 : 4
# 2 / 2 = 1 : 5
# 1 - 1 = 0 : 6

def reduce_number(nums):

    count = 0

    while nums > 0:
        if nums % 2 == 0:
            nums = nums // 2
        else:
            nums = nums - 1
        count += 1

    return count

# check prime number

def check_prime(nums):

    if nums > 1:

        for i in range(2,nums):
            if (nums % i ) == 0:
                print(nums,"is not a prime number")
                print(i,"time",nums//i,"is",nums)
                break
        else:
            print(nums,"is a prime number")

    else:
        print(nums,"is not a prime number")

# Sort Python Dictionaries by Key or Value

def dictionary():

    key_value = {}

    key_value[2] = '64'       
    key_value[1] = '69'
    key_value[4] = '23'
    key_value[5] = '65'
    key_value[6] = '34'
    key_value[3] = '76'

    print('Task 1: -\n')
    print("Keys are")

    for i in sorted(key_value.keys()):
        print(i, end=" ")
        print(" ")
    
def main():
    dictionary()

if __name__=="__main__":
    main()