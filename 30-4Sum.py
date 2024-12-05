# 4sum
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  # Step 1: Sort the array
        quadruplets = []
        n = len(nums)
        
        # Loop for the first element
        for i in range(n - 3):
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Loop for the second element
            for j in range(i + 1, n - 2):
                # Skip duplicates for the second element
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # Two pointers for the remaining two elements
                left, right = j + 1, n - 1
                
                while left < right:
                    curr_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if curr_sum == target:
                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Skip duplicates for the third element
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # Skip duplicates for the fourth element
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        
                        left += 1
                        right -= 1
                    
                    elif curr_sum < target:
                        left += 1  # Move left pointer to increase sum
                    else:
                        right -= 1  # Move right pointer to decrease sum
        
        return quadruplets


# Time Complexity = O(n^3)
# Space Complexity = O(n^3)