"""

[[1,3],[2,6],[8,10],[15,18]]
                       |

1,6 8,10 15,18


"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        result = []
        for interval in intervals:
            if len(result)==0:
                result.append(interval)
            elif interval[0]<=result[-1][1]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)
        return result