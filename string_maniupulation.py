

class Solution:
    def sumOddLength(self,arr):
        s = 0
        for i in range(0,len(arr)):
            for j in range(i,len(arr),2):
                s+=sum(arr[i:j+1])
        return s


obj = Solution()
print(obj.sumOddLength([1,4,2,5,3]))