# isomorphic strings

from collections import defaultdict

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_hash = defaultdict(lambda: 0)
        t_hash = defaultdict(lambda: 0)
        s_arr = []
        t_arr = []

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]

            if s_hash[char_s] != t_hash[char_t]:
                return False

            s_hash[char_s] = i + 1
            t_hash[char_t] = i + 1

        return True