# roman to integer
class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            "I": 1,
            "V": 5,
            "X": 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        for i in range(len(s) - 1):
            if m[s[i]] < m[s[i + 1]]:
                total -= m[s[i]]
            else:
                total += m[s[i]]
        return total + m[s[-1]]
    
# Time Complexity: O(n)
# Space Complexity:O(1)