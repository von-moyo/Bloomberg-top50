# validate binary search tree
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low=float('-inf'), high=float('inf')):
            # An empty node is considered valid
            if not node:
                return True
            # The current node's value must be within the range (low, high)
            if not (low < node.val < high):
                return False
            # Recursively validate the left and right subtrees
            return (validate(node.left, low, node.val) and
                validate(node.right, node.val, high))
        return validate(root)
    
# Time Complexity: O(n)
# Space Complexity: O(h)where 
# ℎ is the height of the tree, due to the recursion stack. For a balanced tree, 
# ℎ = 𝑂(log𝑛), and for a completely unbalanced tree, h=O(n).

# Code Breakdown
# 1. The validate Helper Function
# python
# Copy code
# def validate(node, low=float('-inf'), high=float('inf')):
# Parameters:
# node: The current tree node being validated.
# low: The lower bound for the value of node.val.
# high: The upper bound for the value of node.val.
# Initial Values:
# low is initialized to negative infinity, meaning no lower bound initially.
# high is initialized to positive infinity, meaning no upper bound initially.
# 2. Base Case
# python
# Copy code
# if not node:
#     return True
# If the node is None (empty subtree), it's considered valid because there are no values to violate BST properties.
# 3. Validate the Current Node
# python
# Copy code
# if not (low < node.val < high):
#     return False
# The value of the node must lie in the range (low, high). If it doesn't, the tree is invalid, so return False.
# 4. Recursively Validate Subtrees
# python
# Copy code
# return (validate(node.left, low, node.val) and
#         validate(node.right, node.val, high))
# Left Subtree:
# The node.left must have values in the range (low, node.val).
# Right Subtree:
# The node.right must have values in the range (node.val, high).
# 5. Initial Call
# python
# Copy code
# return validate(root)
# Start the validation process from the root node with no bounds initially (low = -inf, high = inf).
# Time Complexity
# python
# Copy code
# O(n)
# Each node is visited once, so the time complexity is proportional to the number of nodes in the tree (n).
# Space Complexity
# python
# Copy code
# O(h)
# The recursion stack's depth is proportional to the height of the tree (h).
# For a balanced tree, h = O(log n).
# For a completely unbalanced tree, h = O(n).
# Example
# Input:
# python
# Copy code
#     2
#    / \
#   1   3
# root = TreeNode(2)
# root.left = TreeNode(1)
# root.right = TreeNode(3)
# Execution:
# Validate root (2): -inf < 2 < inf → valid.
# Validate left child (1): -inf < 1 < 2 → valid.
# Validate right child (3): 2 < 3 < inf → valid.
# Output:
# python
# Copy code
# True
# Invalid Example:
# python
# Copy code
#     5
#    / \
#   1   4
#      / \
#     3   6
# Here, 4's left child 3 violates the BST property because 3 is not greater than 5.
# Key Insights
# The low and high bounds are updated dynamically as the recursion progresses, ensuring that the BST property is validated across all subtrees.
# The use of recursion simplifies the implementation and ensures correctness.