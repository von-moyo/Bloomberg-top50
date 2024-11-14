class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # Stack to store pairs (character, frequency)
        
        for char in s:
            # If the last character in the stack is the same as the current character
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1  # Increment the frequency
                # If frequency reaches k, pop the last element from the stack
                if stack[-1][1] == k:
                    stack.pop()
            else:
                # Push new character with frequency 1
                stack.append([char, 1])
        
        # Reconstruct the final string based on characters in the stack
        return ''.join(char * count for char, count in stack)


# Time Complexity: O(n)
# Space Complexity: O(n)