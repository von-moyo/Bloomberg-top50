# Warith Alien Dictionary
"""
Graph Construction: We first map out the relationships 
between the characters by iterating over the list of words.
For each consecutive pair of words, we identify the first mismatch
and establish an edge in the graph.

Cycle Detection: The key idea here is that a cycle in the graph would
make it impossible to find a valid ordering. We detect cycles by 
checking if we can topologically sort the entire graph. 
If any character is left out (i.e., not included in the topological 
order), a cycle exists.

Topological Sort (Kahn’s Algorithm): Kahn’s algorithm is suitable 
because it allows us to efficiently extract a valid order of 
characters. We start with characters that have no dependencies 
(in-degree = 0) and process them. As we remove nodes from the graph, 
we reduce the in-degrees of their neighbors.
"""


from collections import defaultdict, deque
from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Step 1: Build the graph
        graph = defaultdict(set)
        in_degree = defaultdict(int)
        for word in words:
            for char in word:
                in_degree[char]  # Default value is 0, no need to explicitly assign

        
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_len = min(len(word1), len(word2))
            # Check if word2 is a prefix of word1 (invalid ordering)
            if word1[:min_len] == word2[:min_len] and len(word1) > len(word2):
                return ""
            for j in range(min_len):
                if word1[j] != word2[j]:
                    if word2[j] not in graph[word1[j]]:
                        graph[word1[j]].add(word2[j])
                        in_degree[word2[j]] += 1
                    break

        # Step 2: Perform topological sort using Kahn's Algorithm
        chars_with_zero_in_degree = []

        # Iterate through each character in the 'in_degree' dictionary
        for char in in_degree:
            # Check if the in-degree of the current character is 0
            if in_degree[char] == 0:
                # If in-degree is 0, add the character to the list
                chars_with_zero_in_degree.append(char)
        queue = deque(chars_with_zero_in_degree)
        order = []

        while queue:
            char = queue.popleft()
            order.append(char)
            for neighbor in graph[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # If not all characters are in the order, there's a cycle
        if len(order) < len(in_degree):
            return ""

        return "".join(order)


# Time complexity: O(V + E) where V is the number of unique
#  characters (vertices). E is the number of edges (relationships 
# between characters). O(C) where C is the sum of all characters in words
# Space: Storage for the graph (adjacency list) and in-degrees: O(V+E), which simplifies to O(C).