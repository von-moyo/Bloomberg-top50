# number of islands
def num_islands(self, grid: List[List[str]]) -> int:
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    visit = set()
    islands = 0

    def bfs(r, c):
        q = collections.deque()
        visit.add((r, c))
        q.append((r, c))
        while q:
            row, col = q.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (r) in range(rows) and (c) in range(cols) and grid[r][c] == "1" and (r, c) not in visit:
                    q.append((r, c))
                    visit.add((r, c))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visit:
                bfs(r, c)
                islands += 1
    return islands

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Edge case: empty grid
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        num_islands = 0

        def dfs(r, c):
            # Check boundaries and whether the current cell is water ('0')
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return

            # Mark the cell as visited by sinking it
            grid[r][c] = '0'

            # Explore all 4 directions: up, down, left, right
            dfs(r - 1, c)  # Up
            dfs(r + 1, c)  # Down
            dfs(r, c - 1)  # Left
            dfs(r, c + 1)  # Right

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':  # Found an island
                    num_islands += 1  # Increment the count
                    dfs(r, c)  # Sink the entire island

        return num_islands

    

# Time Complexity: 0(R * C)
# Space Complexity: 0(R * C)


# Here's a detailed explanation of the num_islands function, including the role of each variable and line of code.

# Function Purpose
# The function counts the number of "islands" in a 2D grid. An island is a group of horizontally or vertically connected 1s, surrounded by water (0).

# Input and Output
# Input:
# grid: A list of lists (List[List[str]]), where each cell contains "1" (land) or "0" (water).
# Output:
# Returns an integer representing the number of distinct islands.
# Step-by-Step Breakdown
# 1. Handle Edge Case
# python
# Copy code
#     if not grid:
#         return 0
# Purpose: If the input grid is empty (grid == []), return 0 because there are no islands.
# 2. Initialize Variables
# python
# Copy code
#     rows, cols = len(grid), len(grid[0])
#     visit = set()
#     islands = 0
# rows, cols: The dimensions of the grid.
# rows: Number of rows in the grid.
# cols: Number of columns in the grid.
# visit: A set to track visited cells. This prevents revisiting cells, ensuring each cell is processed only once.
# islands: Counter for the number of islands found.
# 3. Breadth-First Search (BFS) Helper Function
# python
# Copy code
#     def bfs(r, c):
#         q = collections.deque()
#         visit.add((r, c))
#         q.append((r, c))
# Purpose: Explore all land cells connected to a given starting cell (r, c) using BFS.
# Key Points:
# q: A deque (double-ended queue) used for BFS traversal.
# visit.add((r, c)): Marks the starting cell as visited.
# q.append((r, c)): Adds the starting cell to the BFS queue.
# 4. BFS Traversal
# python
# Copy code
#         while q:
#             row, col = q.popleft()
#             directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
#             for dr, dc in directions:
#                 r, c = row + dr, col + dc
#                 if (r) in range(rows) and (c) in range(cols) and grid[r][c] == "1" and (r, c) not in visit:
#                     q.append((r, c))
#                     visit.add((r, c))
# BFS Loop:
# q.popleft(): Removes the first cell from the queue for processing.
# directions: A list of four possible movement directions: up, down, left, and right.
# For each direction:
# r, c = row + dr, col + dc: Computes the neighboring cell coordinates.
# Conditions:
# (r) in range(rows) and (c) in range(cols): Checks if the neighboring cell is within grid boundaries.
# grid[r][c] == "1": Ensures the neighboring cell is land.
# (r, c) not in visit: Ensures the cell hasn't been visited yet.
# If all conditions are met:
# q.append((r, c)): Adds the neighboring cell to the BFS queue.
# visit.add((r, c)): Marks the neighboring cell as visited.
# 5. Main Loop to Find Islands
# python
# Copy code
#     for r in range(rows):
#         for c in range(cols):
#             if grid[r][c] == "1" and (r, c) not in visit:
#                 bfs(r, c)
#                 islands += 1
# Outer Loop (for r in range(rows)): Iterates through each row of the grid.
# Inner Loop (for c in range(cols)): Iterates through each column of the current row.
# Condition (if grid[r][c] == "1" and (r, c) not in visit):
# Checks if the current cell is land and hasn't been visited yet.
# If true:
# bfs(r, c): Calls the BFS helper function to explore the island starting from the current cell.
# islands += 1: Increments the island counter.
# 6. Return the Result
# python
# Copy code
#     return islands
# Returns the total count of islands.
# Time Complexity
# python
# Copy code
# # Time Complexity: O(R * C)
# Reason:
# Each cell is processed once when visited.
# The BFS traversal visits every cell in an island exactly once.
# Total cells = R * C (rows × columns).
# Space Complexity
# python
# Copy code
# # Space Complexity: O(R * C)
# Reason:
# visit: Stores up to R * C visited cells.
# BFS Queue: At worst, all cells of an island could be in the queue simultaneously, which is proportional to the size of the grid.
# Example Execution
# Input:
# python
# Copy code
# grid = [
#     ["1", "1", "0", "0"],
#     ["1", "1", "0", "0"],
#     ["0", "0", "1", "1"],
#     ["0", "0", "1", "1"]
# ]
# Output:
# The grid has 2 islands:
# First island: Top-left group of 1s.
# Second island: Bottom-right group of 1s.
# Explanation:
# BFS starts at (0, 0) and explores the first island, marking all connected 1s as visited.
# After completing the first island, the loop continues to find the next unvisited land cell (grid[2][2]).
# BFS explores the second island.
# Finally, the function returns 2.