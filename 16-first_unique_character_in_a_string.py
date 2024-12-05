# first unique character in a string

from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_hash = defaultdict(int)
        
        for i in range(len(s)):   # Count occurrences of each character
            char_hash[s[i]] += 1

        print(char_hash)
        print(len(char_hash))

        for i in range(len(s)):
            if char_hash[s[i]] == 1:  # Find the first character with a count of 1
                return i
        return -1


# Time Complexity: O(n)
# Space Complexity: O(k)