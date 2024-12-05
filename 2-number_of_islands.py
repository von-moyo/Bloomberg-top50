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