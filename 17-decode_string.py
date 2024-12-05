# first unique character in a string
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

# Implement the solution under this comment
class Solution:
    def decodeString(self, s: str) -> str:

        stack = [["", 1]]
        curr_num = 0
        
        for char in s:

            if char.isnumeric():
                curr_num = (10 * curr_num) + int(char)

            elif char == "[":
                stack.append(["", curr_num])
                curr_num = 0
            
            elif char.isalpha():
                stack[-1][0]+=char

            elif char == "]":
                last_count, last_char = stack.pop()
                full_char = last_char * last_count
                stack[-1][0] += full_char

        return stack[0][0]

# Time Complexity: O(n)
# Space Complexity: O(n)