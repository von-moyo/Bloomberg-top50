"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # if head is there, i.e. the linked list is not empty
        if head:
            self.flattenHelper(head)
        return head
    
    def flattenHelper(self, head):
        curr, tail = head, head

        while curr:
            child = curr.child
            nxt = curr.next # so that we can return the next of child_tail as the next we stored
            
            if child:
                child_tail = self.flattenHelper(child)
            
                child_tail.next = nxt
                if nxt: 
                    nxt.prev = child_tail
                    
                curr.next = child
                child.prev = curr
                
                curr.child = None
                
                curr = child_tail
            
            # if there is no child
            else: curr = nxt
                
            if curr: 
                tail = curr # tail cannot be null because tail will always be there because it is running when we have a child
                
        return tail

# Time Complexity: O(n), where n is the total number of nodes in the entire multilevel list.
# Space Complexity: O(d), where d is the depth of the deepest child list.
# The recursive calls to flattenHelper consume stack space proportional to the depth of recursion.
# In the worst case, if the child lists are deeply nested, this could be up to O(n), but typically it’s much smaller than n if the list is not deeply nested.