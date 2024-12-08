# minimum remove to make valid parentheses
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []  # Stack to hold indices of unmatched '('
        valid = list(s)  # Convert string to list for easy modification

        # First pass: mark invalid closing parentheses
        for i in range(len(valid)):
            if valid[i] == "(":
                stack.append(i)  # Store index of '('
            elif valid[i] == ")":
                if stack:
                    stack.pop()  # Valid pair found, pop the stack
                else:
                    valid[i] = ""  # Mark unbalanced ')' for removal

        # Second pass: mark unmatched opening parentheses
        for idx in stack:
            valid[idx] = ""  # Mark unbalanced '(' for removal

        # Join and return the valid string
        return "".join(valid)


# time complexity: O(n)
# space complexity: O(n)