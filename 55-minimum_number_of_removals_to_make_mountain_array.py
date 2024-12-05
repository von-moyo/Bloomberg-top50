# minimum number of removals to make mountain array
class Solution:
    def minimumRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Edge case: if the array has fewer than 3 elements, it cannot form a mountain.
        if n < 3:
            return 0
        
        # Step 1: Compute LIS ending at each index
        increasing = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    increasing[i] = max(increasing[i], increasing[j] + 1)
        
        # Step 2: Compute LDS starting at each index
        decreasing = [1] * n
        for i in range(n - 2, -1, -1):
            for j in range(n - 1, i, -1):
                if nums[i] > nums[j]:
                    decreasing[i] = max(decreasing[i], decreasing[j] + 1)
        
        # Step 3: Find the maximum valid mountain subsequence
        max_valid_length = 0
        for i in range(1, n - 1):
            if increasing[i] > 1 and decreasing[i] > 1:  # Only consider i as a peak if it can form a valid mountain
                max_valid_length = max(max_valid_length, increasing[i] + decreasing[i] - 1)
        
        # Step 4: The minimum number of removals is the total number of elements minus the length of the valid mountain subsequence
        return n - max_valid_length


# Time Complexity: O(n^2)
# Space Complexity: O(n)