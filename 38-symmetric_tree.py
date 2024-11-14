class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        # Helper function to check if two trees are mirrors of each other
        def isSymmetricHelper(left: TreeNode, right: TreeNode) -> bool:
            # Base case: both are None
            if not left and not right:
                return True
            # If one is None and the other is not, not symmetric
            if not left or not right:
                return False
            # Check if current nodes match, and recursively check the subtrees
            return (left.val == right.val) and \
                   isSymmetricHelper(left.left, right.right) and \
                   isSymmetricHelper(left.right, right.left)
        
        return isSymmetricHelper(root.left, root.right)


time: O(n)
space: O(n)