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





