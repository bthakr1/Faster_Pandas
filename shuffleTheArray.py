from IPython import get_ipython

nums = [2,5,1,3,4,7]

n = 3


def shuffle(nums,n):
    ans = []

    for i in range(n):
        ans.append(nums[i])
        ans.append(nums[i+n])
    return ans

def inPlaceShuffle(nums,n):
    return [j for i in zip(nums[:n], nums[n:]) for j in i ]

