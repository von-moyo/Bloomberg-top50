from collections import deque

def get_cheapest_cost_bfs(rootNode):
    # Edge case: If the root is None, return 0
    if not rootNode:
        return 0

    # Queue for BFS: stores (current_node, cumulative_cost)
    queue = deque([(rootNode, rootNode.cost)])
    min_cost = float('inf')

    while queue:
        node, current_cost = queue.popleft()

        # If it's a leaf node, check if this path is the cheapest
        if not node.children:
            min_cost = min(min_cost, current_cost)
            continue

        # Add all children to the queue
        for child in node.children:
            queue.append((child, current_cost + child.cost))

    return min_cost

print("Minimum Sales Path Cost (BFS):", get_cheapest_cost_bfs(root))  # Output: 7

# Time: O(n) where n nodes are all at the same level (e.g., a very wide tree).
# Time: O(w) where w is the maximum width of the tree