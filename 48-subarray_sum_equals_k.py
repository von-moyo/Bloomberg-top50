# subarray sum equals k
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = {0: 1}  # Initialize with 0 to handle the case where a prefix sum equals k
        current_sum = 0
        count = 0

        for num in nums:
            current_sum += num
            # Check if there's a prefix sum that would result in a subarray summing to k
            if current_sum - k in prefix_sums:
                count += prefix_sums[current_sum - k]

            # Update the hash map with the current prefix sum
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1

        return count


# Time Complexity: O(n) because we make a single pass through nums.
# Space Complexity: O(n) for the hash map storing prefix sums.