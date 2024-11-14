class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])

        result = []

        for interval in intervals:
            if not result:
                result.append(interval)
            if interval[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)

        return result
    

# Time Complexity: O(nlogn)+O(n)=O(nlogn)
# Space Complexity: O(n)
