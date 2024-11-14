class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:
    def __init__(self):
        self.key_count = {}
        self.count_nodes = {}
        self.head = Node(float('-inf'))  # Dummy head for min node
        self.tail = Node(float('inf'))   # Dummy tail for max node
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node_after(self, new_node, prev_node):
        """Insert a new_node after prev_node in the doubly linked list."""
        new_node.prev = prev_node
        new_node.next = prev_node.next
        prev_node.next.prev = new_node
        prev_node.next = new_node

    def _remove_node(self, node):
        """Remove a node from the doubly linked list."""
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.count_nodes[node.count]

    def inc(self, key: str) -> None:
        curr_count = self.key_count.get(key, 0)
        new_count = curr_count + 1
        self.key_count[key] = new_count

        # Move key to the next count node
        if new_count not in self.count_nodes:
            self.count_nodes[new_count] = Node(new_count)
            self._add_node_after(self.count_nodes[new_count], 
                                 self.count_nodes.get(curr_count, self.head))

        # Add key to new count node and remove from old count node
        self.count_nodes[new_count].keys.add(key)
        if curr_count > 0:
            self.count_nodes[curr_count].keys.remove(key)
            if not self.count_nodes[curr_count].keys:
                self._remove_node(self.count_nodes[curr_count])

    def dec(self, key: str) -> None:
        curr_count = self.key_count[key]
        new_count = curr_count - 1
        if new_count == 0:
            del self.key_count[key]
        else:
            self.key_count[key] = new_count

        # Move key to the previous count node or remove it
        if new_count > 0:
            if new_count not in self.count_nodes:
                self.count_nodes[new_count] = Node(new_count)
                self._add_node_after(self.count_nodes[new_count], 
                                     self.count_nodes[curr_count].prev)
            self.count_nodes[new_count].keys.add(key)

        # Remove key from current count node
        self.count_nodes[curr_count].keys.remove(key)
        if not self.count_nodes[curr_count].keys:
            self._remove_node(self.count_nodes[curr_count])

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))




# Time Complexity = O(1)
# Space Complexity = O(n)