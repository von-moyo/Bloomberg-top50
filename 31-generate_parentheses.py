# generate parentheses

def generateParenthesis(self, n: int) -> List[str]:
    def dfs(left, right, s):
        # Base case: if the current string length is 2 * n, add to result
        if len(s) == n * 2:
            res.append(s)
            return

        # Add an opening parenthesis if we haven't reached the limit
        if left < n:
            dfs(left + 1, right, s + '(')

        # Add a closing parenthesis if it would not exceed the number of open ones
        if right < left:
            dfs(left, right + 1, s + ')')

    res = []
    dfs(0, 0, '')  # Initialize DFS with 0 left and right parentheses and empty string
    return res

# Time Complexity - O((4^n)/root n)
# Space Complexity - O((4^n)/root n)