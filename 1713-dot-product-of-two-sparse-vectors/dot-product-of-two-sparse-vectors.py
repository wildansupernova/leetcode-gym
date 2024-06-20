"""
[0,3,0,4,0]

"""

class SparseVector:
    def __init__(self, nums: List[int]):
        pairs = []
        for i in range(len(nums)):
            pairs.append((i, nums[i]))
        self.pairs = pairs
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        i = 0
        j = 0
        while i<len(self.pairs) and j<len(vec.pairs):
            if self.pairs[i][0]==vec.pairs[j][0]:
                result += self.pairs[i][1]*vec.pairs[j][1]
                i+=1
                j+=1
            elif self.pairs[i][0]<vec.pairs[j][0]:
                i+=1
            else:
                j+=1
        return result

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)