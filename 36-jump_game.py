
from collections import defaultdict

# Correct Approach: Union-Find with DFS
# To solve this, you need to build a graph where:

# Each node represents a variable.
# An edge between two nodes represents the relationship between them (like an equation).
# The Union-Find (or Disjoint Set Union, DSU) structure is useful here. It helps to find connected components in the graph. We can use DFS to calculate the result of the division of variables in the same connected component.

# Approach:
# Union-Find Setup:

# Use a union-find data structure to group variables that are connected via equations.
# Store the value ratios for each node to its parent node.
# DFS for Queries:

# For each query, check if both variables belong to the same connected component.
# If they do, perform DFS to find the product of the ratios along the path between the two variables.
# Steps:
# Build the graph by processing the equations and their corresponding values.
# For each query, use DFS to find the ratio between the two variables, if they belong to the same connected component.
# Explanation:
# Union-Find Setup:

# We maintain a parent dictionary to store the parent of each variable.
# We also store the ratio dictionary to track the ratio of each node to its parent (important for answering queries).
# Find Method:

# The find method uses path compression to find the root of a node and updates the ratio of the node relative to the root.
# Union Method:

# The union method connects two nodes by setting the root of one node to the root of the other, and adjusts the ratio to maintain the relationship between the two nodes.
# Calculating Equations:

# For each query, we use the find method to check if both nodes belong to the same connected component. If they do, we compute the ratio of the two nodes based on their paths in the union-find structure.
# Edge Cases:

# If either of the variables in the query is not present in the parent dictionary, it means they were not part of any equation, so we return -1.0.
# If the two nodes are not connected, we return -1.0.
class Solution:
    def __init__(self):
        self.parent = {}
        self.ratio = {}

    def find(self, node: str) -> str:
        if node != self.parent.get(node, node):
            orig_parent = self.parent[node]
            self.parent[node] = self.find(self.parent[node])
            self.ratio[node] *= self.ratio[orig_parent]
        return self.parent.get(node, node)

    def union(self, node1: str, node2: str, value: float):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            self.parent[root1] = root2
            self.ratio[root1] = value * self.ratio[node2] / self.ratio[node1]

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Initialize the Union-Find structure
        for (a, b), value in zip(equations, values):
            if a not in self.parent:
                self.parent[a] = a
                self.ratio[a] = 1.0
            if b not in self.parent:
                self.parent[b] = b
                self.ratio[b] = 1.0

            # Union the two variables
            self.union(a, b, value)

        # Answer the queries
        result = []
        for a, b in queries:
            if a not in self.parent or b not in self.parent:
                result.append(-1.0)
            else:
                root_a = self.find(a)
                root_b = self.find(b)
                if root_a == root_b:
                    result.append(self.ratio[a] / self.ratio[b])
                else:
                    result.append(-1.0)

        return result


Time: O(n)
Space: O(1)