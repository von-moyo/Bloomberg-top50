# lru cache
# LRUCache
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right 
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
        
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popItem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# time complexity = 0(1)
# space complexity = 0(capacity)

# Explanation of the LRUCache Class
# The LRUCache implements a Least Recently Used (LRU) Cache, which allows for efficient storage and retrieval of key-value pairs, while evicting the least recently used items when the cache exceeds its capacity. It achieves this with a combination of a hashmap and a doubly linked list.

# Code Breakdown
# 1. Node Class
# python
# Copy code
# class Node:
#     def __init__(self, key, val):
#         self.key, self.val = key, val
#         self.prev = self.next = None
# Represents an individual cache entry with:
# key: The unique key for the cache entry.
# val: The value associated with the key.
# prev: A pointer to the previous node in the doubly linked list.
# next: A pointer to the next node in the doubly linked list.
# 2. LRUCache Initialization
# python
# Copy code
# def __init__(self, capacity: int):
#     self.cap = capacity
#     self.cache = {}  # Hashmap to store key-to-node mapping
#     self.left, self.right = Node(0, 0), Node(0, 0)  # Dummy nodes
#     self.left.next, self.right.prev = self.right, self.left
# Attributes:
# self.cap: Maximum capacity of the cache.
# self.cache: A dictionary (hashmap) to map keys to Node objects for constant-time access.
# self.left and self.right: Dummy nodes that act as sentinels for the doubly linked list.
# self.left represents the least recently used (LRU) end.
# self.right represents the most recently used (MRU) end.
# 3. Helper Methods
# a. Remove a Node
# python
# Copy code
# def remove(self, node):
#     prev, nxt = node.prev, node.next
#     prev.next, nxt.prev = nxt, prev
# Removes a node from the doubly linked list by:
# Re-linking its previous (prev) and next (next) neighbors.
# b. Insert a Node
# python
# Copy code
# def insert(self, node):
#     prev, nxt = self.right.prev, self.right
#     prev.next = nxt.prev = node
#     node.next, node.prev = nxt, prev
# Inserts a node just before the self.right (MRU end) by:
# Adjusting pointers of node and its neighbors.
# 4. Get Method
# python
# Copy code
# def get(self, key: int) -> int:
#     if key in self.cache:
#         self.remove(self.cache[key])  # Remove the node from its current position
#         self.insert(self.cache[key])  # Move the node to the MRU end
#         return self.cache[key].val  # Return the value
#     return -1  # Key is not in the cache
# Retrieves the value for key from the cache:
# If the key exists:
# The corresponding Node is moved to the MRU end to mark it as recently used.
# Return the value (val) of the node.
# If the key does not exist, return -1.
# 5. Put Method
# python
# Copy code
# def put(self, key: int, value: int) -> None:
#     if key in self.cache:
#         self.remove(self.cache[key])  # Remove the old node if it exists
#     self.cache[key] = Node(key, value)  # Create a new node and add it to the cache
#     self.insert(self.cache[key])  # Move it to the MRU end

#     if len(self.cache) > self.cap:
#         lru = self.left.next  # Identify the least recently used node
#         self.remove(lru)  # Remove the LRU node from the linked list
#         del self.cache[lru.key]  # Remove the LRU node from the hashmap
# Adds or updates a key-value pair in the cache:
# If the key exists:
# Remove the old node and update it with the new value.
# Add the new node to the MRU end.
# If the cache size exceeds self.cap, evict the least recently used (lru) node:
# Remove the node from the linked list.
# Delete the entry from the cache dictionary.
# How It Works
# Doubly Linked List:
# Maintains the order of usage.
# The left node points to the least recently used (LRU) node.
# The right node points to the most recently used (MRU) node.
# Hashmap:
# Provides constant-time access to Node objects by their keys.
# Eviction:
# When the cache exceeds its capacity, the least recently used item (node next to self.left) is removed from both the linked list and the hashmap.
# Time Complexity
# get: 
# 𝑂
# (
# 1
# )
# O(1), constant-time lookup in the hashmap and updates in the doubly linked list.
# put: 
# 𝑂
# (
# 1
# )
# O(1), constant-time insertion, removal, and hashmap operations.
# Space Complexity
# 𝑂
# (
# 𝑐
# 𝑎
# 𝑝
# 𝑎
# 𝑐
# 𝑖
# 𝑡
# 𝑦
# )
# O(capacity):
# The hashmap and doubly linked list store up to capacity nodes.
# Example
# Input:
# python
# Copy code
# cache = LRUCache(2)
# cache.put(1, 1)
# cache.put(2, 2)
# print(cache.get(1))  # Outputs: 1
# cache.put(3, 3)      # Evicts key 2
# print(cache.get(2))  # Outputs: -1
# cache.put(4, 4)      # Evicts key 1
# print(cache.get(1))  # Outputs: -1
# print(cache.get(3))  # Outputs: 3
# print(cache.get(4))  # Outputs: 4
# Execution:
# Add (1, 1), (2, 2) → Cache: {1: Node(1, 1), 2: Node(2, 2)}.
# Access key 1 → Move 1 to MRU end → Cache: {2, 1}.
# Add (3, 3) → Evict key 2 → Cache: {1, 3}.
# Access key 2 → Return -1.
# Add (4, 4) → Evict key 1 → Cache: {3, 4}.
# Access keys → 3: 3, 4: 4.