class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        # Calculate the mask for maximum bit constraint (all bits set to 1 within maximumBit range)
        max_val = (1 << maximumBit) - 1  # Equivalent to 2^maximumBit - 1
        
        # Calculate the XOR of all elements in nums
        current_xor = 0
        for num in nums:
            current_xor ^= num
            
        # Process each query from the end of nums
        result = []
        for i in range(len(nums) - 1, -1, -1):
            # Compute k as the bitwise complement within the max_val range
            result.append(max_val ^ current_xor)
            
            # Remove the last element from nums for the next query by updating current_xor
            current_xor ^= nums[i]
        
        return result



# Time Complexity: O(n)
# Space Complexity: O(n)