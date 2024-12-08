# top k frequent words

from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        # return [key for key, val in freq.most_common(k)]
        heap = []
        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for count, num in heap]
# Time Complexity:
# Counting Frequencies: O(n), where 𝑛 is the number of words.
# Heap Operations:Building the heap takes O(m), where m is the number of unique words. Extracting the top k elements takes O(klogm).
# Thus, the overall time complexity is O(n+m+klogm), which is efficient for large inputs.
    

# Space Complexity:
# Counter and Heap: Storing word frequencies and heap elements requires O(m) space.
# Result List: The result list for the top k words requires O(k) space.
# So, the overall space complexity is O(m+k).