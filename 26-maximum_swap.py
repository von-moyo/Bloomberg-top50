class Solution:
    def maximumSwap(self, num: int) -> int:
        # Convert the number to a list of digits
        digits = list(str(num))
        ["1", "2", "1"]
        
        # Create a map to store the last index of each digit
        last_index = {}
        for idx in range(len(digits)):
            last_index[int(digits[idx])] = idx
        
        # Traverse the digits
        for i in range(len(digits)):
            # Try to find a larger digit from the right side to swap with
            for d in range(9, int(digits[i]), -1):
                if d in last_index and last_index[d] > i:
                    # Swap the digits
                    digits[i], digits[last_index[d]] = digits[last_index[d]], digits[i]
                    return int(''.join(digits))  # Return the result as an integer
        
        return num  # Return the number if no swap was done

# Time Complexity = O(n)
# Space Complexity = O(n)