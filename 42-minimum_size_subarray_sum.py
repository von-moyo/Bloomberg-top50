# To solve the problem of finding the minimal length of a subarray whose sum is greater than or equal to the target, we can use a sliding window approach, which ensures an optimal solution with a time complexity of O(n).

# Thought Process:
# Sliding Window Approach:

# This approach involves using two pointers (left and right) to represent the window of the current subarray. We will expand the window by moving the right pointer and include more elements in the sum. Once the sum of the current window exceeds or equals the target, we try to shrink the window by moving the left pointer to the right while keeping the sum valid (i.e., greater than or equal to the target).
# Steps:

# Start with both left and right pointers at the beginning of the array.
# Expand the window by moving the right pointer and adding the elements to the current sum.
# Once the sum is greater than or equal to the target, check the length of the current subarray and update the minimum length if needed.
# Move the left pointer to shrink the window and check if the sum is still greater than or equal to the target.
# Continue this process until we've processed the entire array.
# Edge Case:

# If no subarray with a sum greater than or equal to the target exists, return 0.
# Time Complexity:
# O(n): The sliding window approach ensures that each element is processed at most twice (once when expanding the window with the right pointer and once when shrinking the window with the left pointer).
# Space Complexity:
# O(1): We only use a few extra variables for tracking the sum, left pointer, right pointer, and the minimum length.
# Python Code:
# python
# Copy code
# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         n = len(nums)
#         left = 0
#         current_sum = 0
#         min_length = float('inf')  # Initialize with a very large number
        
#         for right in range(n):
#             current_sum += nums[right]  # Expand the window by including nums[right]
            
#             # When the sum of the window is >= target, try to shrink the window
#             while current_sum >= target:
#                 min_length = min(min_length, right - left + 1)
#                 current_sum -= nums[left]  # Shrink the window by excluding nums[left]
#                 left += 1
        
#         return min_length if min_length != float('inf') else 0  # If no valid subarray is found, return 0
# Explanation:
# Initial Setup:

# left: Pointer to the start of the current subarray.
# current_sum: Keeps track of the sum of the current subarray.
# min_length: Stores the minimal length of a valid subarray (initialized to infinity).
# Main Loop (for right in range(n)):

# For each element in the array (indexed by right), add its value to current_sum to expand the window.
# Shrink the Window:

# Once current_sum >= target, the window is valid, and we try to shrink it by moving left to the right. During this process, we check if the current subarray is smaller than the previous minimum length and update min_length.
# Return the Result:

# If no subarray with a sum greater than or equal to the target is found, we return 0. Otherwise, we return the minimal length stored in min_length.

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        current_sum = 0
        min_length = float('inf')  # Initialize with a very large number
        
        for right in range(n):
            current_sum += nums[right]  # Expand the window by including nums[right]
            
            # When the sum of the window is >= target, try to shrink the window
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]  # Shrink the window by excluding nums[left]
                left += 1
        
        return min_length if min_length != float('inf') else 0  # If no valid subarray is found, return 0


# time = O(n)
# space = O(1)