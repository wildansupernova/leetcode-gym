"""
1 4

"""
import random


class Solution: 


    def __init__(self, w: List[int]):
        self.prefix = [w[0]]
        for i in range(1, len(w)):
            self.prefix.append(w[i]+self.prefix[-1])

    def getRandom(self, left, right):
        return random.uniform(left,right)

    def pickIndex(self) -> int:
        left = 0
        right = len(self.prefix)-1
        target = self.getRandom(0, self.prefix[-1])
        while left<right:
            mid = left + (right-left)//2
            if self.prefix[mid]<target:
                left = mid + 1
            else:
                right = mid
        if self.prefix[left]<target:
            left+=1
        return left
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()