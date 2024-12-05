# minimum absolute difference
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # Step 1: Sort the array
        arr.sort()
        
        # Step 2: Find the minimum absolute difference
        min_diff = float('inf')
        for i in range(len(arr) - 1):
            min_diff = min(min_diff, arr[i + 1] - arr[i])
        
        # Step 3: Collect all pairs with this minimum difference
        result = []
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] == min_diff:
                result.append([arr[i], arr[i + 1]])
        
        # Step 4: Return the result
        return result
    


# Time Complexity:O(nlogn)
# Space Complexity: O(n)