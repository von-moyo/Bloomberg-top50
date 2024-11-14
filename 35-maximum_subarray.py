class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]  # Initialize max_sum to the first element
        current_sum = nums[0]  # Initialize current_sum to the first element
        
        for num in nums[1:]:  # Start from the second element
            current_sum = max(num, current_sum + num)  # Update current subarray sum
            max_sum = max(max_sum, current_sum)  # Update max sum found so far
        
        return max_sum


# Time Complexity = O(n)
# Space Complexity = O(1)