from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Define the binary search range
        left, right = 1, max(piles)
        
        while left < right:
            mid = (left + right) // 2  # Proposed eating speed `k`
            hours_needed = 0
            
            # Calculate total hours needed at speed `mid`
            for pile in piles:
                hours_needed += (pile + mid - 1) // mid  # Equivalent to `math.ceil(pile / mid)`
            
            # If hours needed is within the limit, search the left half for possibly smaller `k`
            if hours_needed <= h:
                right = mid
            else:  # If hours needed exceeds limit, `mid` is too slow
                left = mid + 1
        
        return left



# Approach: Using binary search over the range of possible speeds

# Time Complexity: O(n⋅log(m))
# Space Complexity: O(1)