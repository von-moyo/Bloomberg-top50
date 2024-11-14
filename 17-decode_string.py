class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != "]":
                stack.append(char)
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k

                stack.append(int(k) * substr)
        return "".join(stack) 
    

# Time Complexity: This solution still operates in O(n×k) in the worst case because we process each character once, and nested repetitions still take O(n×k) time due to string expansion.
# Space Complexity: The stack’s worst-case space complexity remains O(n×k) if every character is nested deeply.