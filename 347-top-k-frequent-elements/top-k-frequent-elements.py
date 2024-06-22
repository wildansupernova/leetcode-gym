"""
1. count the frequencies
   1 -> 3 <
   2 -> 2
   3 -> 1
2. Aproach 1 - > sorting ->  nlog n
3. Aproach 2 ->. min heap ->  n log k
    2 1 
4. Approach 3 -> quick selct -> avg O(n) , avg O(n^2)

left
right


"""
import random


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = defaultdict(int)
        for num in nums:
            count[num]+=1
        keys = [ key for key in count ]

        def partition(left,right, arr):
            pickIndex = random.randint(left,right)
            arr[pickIndex], arr[right] = arr[right], arr[pickIndex]
            pivot = left
            for i in range(left,right):
                if count[arr[i]]>=count[arr[right]]:
                    arr[i], arr[pivot] = arr[pivot], arr[i]
                    pivot+=1
            arr[pivot], arr[right] = arr[right], arr[pivot]
            return pivot

        k-=1
        left = 0
        right = len(keys)-1

        while True:
            pivot = partition(left,right, keys)
            if pivot==k:
                return keys[:k+1]
            elif k<pivot:
                right = pivot-1
            else:
                left = pivot+1