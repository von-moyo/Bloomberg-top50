class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        # Start from the root
        level_start = root
        
        # Traverse level by level
        while level_start.left:
            current = level_start
            
            # Connect nodes in the current level
            while current:
                # Connect the left child to the right child
                current.left.next = current.right
                
                # If current node has a next node, connect right child to next's left child
                if current.next:
                    current.right.next = current.next.left
                
                # Move to the next node in the current level
                current = current.next
            
            # Move to the next level (leftmost node of the next level)
            level_start = level_start.left
        
        return root


# Time Complexity: O(N)
# Space Complexity: O(1)