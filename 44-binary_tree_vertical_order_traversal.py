from collections import defaultdict, deque
from typing import Optional, List


# To solve the vertical order traversal of a binary tree, we can use a Breadth-First Search (BFS) approach. This approach ensures we visit nodes level by level from top to bottom and left to right. By assigning a column index to each node, we can collect nodes based on their vertical position (column).

# Thought Process
# Column Indexing:

# We assign a unique column index to each node:
# The root node starts at column 0.
# The left child of a node is in column - 1.
# The right child of a node is in column + 1.
# This way, nodes in the same vertical column will share the same column index.
# Data Structure:

# Use a dictionary col_table to store nodes by their column index.
# col_table[column] will contain a list of nodes in that column, in top-to-bottom and left-to-right order.
# Use a queue to implement BFS:
# Each element in the queue is a tuple (node, row, column) to keep track of the node, its row, and its column.
# Traversal Logic:

# Start with the root node at row 0 and column 0.
# For each node:
# Insert it into col_table under its column index.
# Add its left child to the queue with column - 1.
# Add its right child to the queue with column + 1.
# After traversing the tree, sort the col_table by columns to maintain left-to-right order in the output.
# Output Construction:

# For each column in sorted order, extract nodes in each column to form the final result.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # Initialize a dictionary to store nodes by their column
        col_table = defaultdict(list)
        # Queue to perform BFS; stores (node, row, column) tuples
        queue = deque([(root, 0, 0)])
        
        while queue:
            node, row, col = queue.popleft()
            if node:
                col_table[col].append((row, node.val))
                # Add left and right children to the queue
                queue.append((node.left, row + 1, col - 1))
                queue.append((node.right, row + 1, col + 1))

        # Sort columns and collect results
        sorted_columns = sorted(col_table.keys())
        result = []
        for col in sorted_columns:
            # Sort by row first and then by node value if necessary
            col_table[col].sort(key=lambda x: x[0])
            result.append([val for _, val in col_table[col]])

        return result



# Time Complexity: O(NlogN)
# Space Complexity: O(N)