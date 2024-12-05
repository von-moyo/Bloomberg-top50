# valid parenthesis
class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to keep track of opening brackets
        stack = []
        
        # Map of matching bracket pairs
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        # Traverse the string
        for char in s:
            if char in bracket_map.values():
                # If the character is an opening bracket, push it to the stack
                stack.append(char)
            elif char in bracket_map:
                # If the character is a closing bracket
                if not stack or stack[-1] != bracket_map[char]:
                    # If stack is empty or the top of the stack doesn't match the current closing bracket
                    return False
                # Pop the matching opening bracket from the stack
                stack.pop()
        
        # If the stack is empty, all brackets were matched correctly
        return not stack

# time complexity: O(n)
# space complexity: O(min(n, m))