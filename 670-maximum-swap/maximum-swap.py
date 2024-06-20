"""
9 9 7 9
2 2 3 n

99554
"""

class Solution:
    def maximumSwap(self, num: int) -> int:
        if num==0: return0
        nums = []
        while num!=0:
            nums.append(num % 10)
            num = num // 10
        nums.reverse()

        biggestIndex = [None]*len(nums)
        curBiggestIndex = len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            biggestIndex[i] = curBiggestIndex
            if nums[i]>nums[curBiggestIndex]:
                curBiggestIndex = i
        
        for i in range(len(nums)-1):
            if nums[i]<nums[biggestIndex[i]]:
                nums[biggestIndex[i]], nums[i] = nums[i], nums[biggestIndex[i]]
                break
        result = 0
        for num in nums:
            result = result*10 + num
        return result
        