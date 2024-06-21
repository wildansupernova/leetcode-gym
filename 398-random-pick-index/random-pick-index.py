import random

class Solution:

    def __init__(self, nums: List[int]):
        self.numIndex = defaultdict(list)
        for i in range(len(nums)):
            self.numIndex[nums[i]].append(i)

    def pick(self, target: int) -> int:
        return random.choices(self.numIndex[target])[0]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)