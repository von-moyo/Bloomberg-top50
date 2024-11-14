class Solution:
    def minChanges(self, s: str) -> int:
        n = len(s)
        res = 0

        for i in range(0, n, 2):
            if s[i] != s[i + 1]:
                res += 1
        return res
    
# Time Complexity: O(n)
# Space Complexity: O(1)