# group anagrams

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_hash = defaultdict(list)
        res_arr = []
        for word in strs:
            sorted_hash[sorted(word)].append(word)
        return list(sorted_hash.values())