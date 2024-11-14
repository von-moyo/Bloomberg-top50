class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetIndex = {}
        for i, num in enumerate(nums):
            if num in targetIndex:
                print(targetIndex)
                return targetIndex[num], i
            else: 
                targetIndex[target-num] = i
        
# Time Complexity: 𝑂(𝑛) n is the number of elements in nums.
# Space Complexity: 𝑂(𝑛) for storing the complements in targetIndex.