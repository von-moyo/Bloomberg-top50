# minimum array end
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res = x           # Initialize res with the value of x
        n -= 1             # Decrease n by 1
        mask = 1           # Initialize mask to 1 (binary: 0001)

        while n > 0:       # Run the loop until n becomes 0
            if (mask & x) == 0:   # If the bitwise AND between mask and x is 0
                res |= (n & 1) * mask  # Set the corresponding bit in res
                n >>= 1               # Right shift n by 1
            mask <<= 1                # Left shift the mask by 1

        return res  # Return the final result

# time complexity = O(log n)
# space complexity = O(1)