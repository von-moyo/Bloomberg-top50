# longest consecutive sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # If the input list is empty, return 0
        if not nums:
            return 0
        
        # Insert all elements in a set for O(1) look-up time
        num_set = set(nums)
        longest_streak = 0
        
        # Iterate through each number
        for num in num_set:
            # Check if it's the start of a new sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                # Expand the sequence
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                # Update the longest streak
                longest_streak = max(longest_streak, current_streak)
        
        return longest_streak


time: O(n)
space: O(n)