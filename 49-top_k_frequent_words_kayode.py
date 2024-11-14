from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words_hash = Counter(words)
        # heap = [(-freq, word) for word, freq in words_hash.items()]
        heap =  []
        res_arr = []
        for word, freq in words_hash.items():
            heap.append((-freq, word))
        print(heap)
        heapq.heapify(heap)
        for _ in range(k):
            res_arr.append(heapq.heappop(heap)[1])
    
        
        return res_arr



# Time Complexity:
# Counting Frequencies: O(n), where 𝑛 is the number of words.
# Heap Operations:Building the heap takes O(m), where m is the number of unique words. Extracting the top k elements takes O(klogm).
# Thus, the overall time complexity is O(n+m+klogm), which is efficient for large inputs.
    

# Space Complexity:
# Counter and Heap: Storing word frequencies and heap elements requires O(m) space.
# Result List: The result list for the top k words requires O(k) space.
# So, the overall space complexity is O(m+k).