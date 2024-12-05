from collections import deque

def can_reach_oasis(grid, gas):
    rows, cols = len(grid), len(grid[0])
    start, target = None, None

    # Locate the car ('c') and oasis ('o') positions
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'c':
                start = (r, c)
            elif grid[r][c] == 'o':
                target = (r, c)

    if not start or not target:
        raise ValueError("Grid must contain both a car ('c') and an oasis ('o').")

    # Early exit if Manhattan distance exceeds gas
    manhattan_distance = abs(start[0] - target[0]) + abs(start[1] - target[1])
    if manhattan_distance > gas:
        return False

    # BFS setup
    queue = deque([(start[0], start[1], gas)])  # (row, col, remaining gas)
    visited = set()
    visited.add((start[0], start[1]))

    while queue:
        row, col, remaining_gas = queue.popleft()

        # If we reach the oasis, return True
        if grid[row][col] == 'o':
            return True

        # Explore neighbors
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Up, Down, Left, Right
            nr, nc = row + dr, col + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and remaining_gas > 0:
                if grid[nr][nc] in {'.', 'o'}:  # Can traverse empty land or oasis
                    visited.add((nr, nc))
                    queue.append((nr, nc, remaining_gas - 1))

    # If we exhaust the queue without finding the oasis
    return False


# Time: O(rows x cols)
# Space: O(rows x cols)