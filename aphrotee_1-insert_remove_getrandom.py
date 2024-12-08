# import random

# class RandomizedSet:

#     def __init__(self):
#         self.arr = []
#         self.dict = {}

#     def insert(self, val: int) -> bool:
#         if val in self.dict: return False

#         self.arr.append(val)
#         self.dict[val] = len(self.arr) - 1
#         return True

#     def remove(self, val: int) -> bool:
#         if val not in self.dict: return False

#         index = self.dict[val]
#         lastValue = self.arr[-1]

#         self.arr[index], self.dict[lastValue] = lastValue, index

#         self.arr.pop()
#         del self.dict[val]
#         return True

#     def getRandom(self) -> int:
#         randomInt = random.randint(0, len(self.arr) - 1)
#         return self.arr[randomInt]

class BrowserHistory:
    class Node:
        """Helper class to represent a doubly linked list node."""
        def __init__(self, url):
            self.url = url
            self.prev = None
            self.next = None
# Insert, Remove, getRandom
import random
class RandomizedSet:

    def __init__(self):
        # Initialize head and tail of the doubly linked list
        self.head = self.Node(None)  # Dummy head
        self.tail = self.Node(None)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

        # Dictionary to store URLs and their corresponding nodes
        self.url_map = {}

    def _remove(self, node):
        """Removes a node from the linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_front(self, node):
        """Adds a node to the front of the linked list (most recent position)."""
        first = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = first
        first.prev = node

    def visit(self, url):
        """Visit a URL, moving it to the most recent position if it already exists."""
        if url in self.url_map:
            # URL already exists, remove it first
            self._remove(self.url_map[url])

        # Create a new node and add it to the front
        new_node = self.Node(url)
        self._add_to_front(new_node)
        self.url_map[url] = new_node

    def get_history(self):
        """Return the browsing history in reverse chronological order."""
        history = []
        current = self.head.next
        while current != self.tail:
            history.append(current.url)
            current = current.next
        return history


# 1. Class Structure
# python
# Copy code
# class BrowserHistory:
# BrowserHistory: Represents a browsing history manager using a doubly linked list (DLL) for efficient operations like adding and removing nodes.
# python
# Copy code
#     class Node:
#         """Helper class to represent a doubly linked list node."""
#         def __init__(self, url):
#             self.url = url
#             self.prev = None
#             self.next = None
# Node: A helper class nested inside BrowserHistory. Each Node represents a webpage (url) and has:
# url: Stores the URL as a string.
# prev: Pointer to the previous node in the DLL.
# next: Pointer to the next node in the DLL.
# 2. Initialization
# python
# Copy code
#     def __init__(self):
#         self.head = self.Node(None)  # Dummy head
#         self.tail = self.Node(None)  # Dummy tail
#         self.head.next = self.tail
#         self.tail.prev = self.head

#         # Dictionary to store URLs and their corresponding nodes
#         self.url_map = {}
# __init__ initializes the BrowserHistory instance.
# Doubly Linked List Setup:
# self.head and self.tail: Dummy nodes to simplify DLL management.
# self.head.next = self.tail: Connects head to tail.
# self.tail.prev = self.head: Connects tail to head.
# The DLL starts empty, so these connections ensure structural integrity.
# self.url_map: A dictionary to map URLs to their respective Node objects. This allows O(1) access to nodes by URL.
# 3. Remove a Node
# python
# Copy code
#     def _remove(self, node):
#         """Removes a node from the linked list."""
#         prev_node = node.prev
#         next_node = node.next
#         prev_node.next = next_node
#         next_node.prev = prev_node
# _remove: Detaches a Node from the DLL.
# prev_node: The node preceding the one being removed.
# next_node: The node following the one being removed.
# prev_node.next = next_node: Skips the removed node, connecting the previous node directly to the next node.
# next_node.prev = prev_node: Updates the previous pointer of the next node to skip the removed node.
# The node being removed is left isolated (its pointers are not updated explicitly but it is disconnected).
# 4. Add a Node to the Front
# python
# Copy code
#     def _add_to_front(self, node):
#         """Adds a node to the front of the linked list (most recent position)."""
#         first = self.head.next
#         self.head.next = node
#         node.prev = self.head
#         node.next = first
#         first.prev = node
# _add_to_front: Inserts a Node at the start of the DLL (after the head dummy node).
# first: The current first real node in the DLL (self.head.next).
# Updates:
# self.head.next = node: Links the dummy head to the new node.
# node.prev = self.head: Points the new node’s prev to the dummy head.
# node.next = first: Points the new node’s next to the old first node.
# first.prev = node: Updates the old first node’s prev to point to the new node.
# 5. Visit a URL
# python
# Copy code
#     def visit(self, url):
#         """Visit a URL, moving it to the most recent position if it already exists."""
#         if url in self.url_map:
#             # URL already exists, remove it first
#             self._remove(self.url_map[url])

#         # Create a new node and add it to the front
#         new_node = self.Node(url)
#         self._add_to_front(new_node)
#         self.url_map[url] = new_node
# visit: Adds a URL to the browsing history.
# if url in self.url_map:: Checks if the URL already exists.
# If it does, its corresponding Node is removed from its current position.
# new_node = self.Node(url): Creates a new Node for the URL.
# self._add_to_front(new_node): Moves the new or updated node to the front of the DLL.
# self.url_map[url] = new_node: Updates the dictionary to reference the new node.
# 6. Get Browsing History
# python
# Copy code
#     def get_history(self):
#         """Return the browsing history in reverse chronological order."""
#         history = []
#         current = self.head.next
#         while current != self.tail:
#             history.append(current.url)
#             current = current.next
#         return history
# get_history: Returns a list of URLs in reverse chronological order (most recent first).
# history = []: Initializes an empty list to store the URLs.
# current = self.head.next: Starts at the first real node in the DLL.
# while current != self.tail:: Iterates through the DLL until the dummy tail is reached.
# history.append(current.url): Adds the URL of the current node to the list.
# current = current.next: Moves to the next node.
# return history: Returns the accumulated history list.
# Key Concepts
# Doubly Linked List:
# Efficient for insertion/removal operations.
# Preserves order for reverse chronological browsing history.
# Dictionary (url_map):
# Enables O(1) access to nodes for quick removal/reordering.
# Advantages
# Efficient operations for maintaining and retrieving browsing history.
# Uses a combination of a DLL and a dictionary for performance optimization.