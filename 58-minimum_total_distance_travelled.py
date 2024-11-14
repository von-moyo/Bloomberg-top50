from itertools import accumulate
from math import inf

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # Step 1: Sort robots and factories by position.
        robot.sort()
        factory.sort()

        n, m = len(robot), len(factory)
        
        # Step 2: Initialize DP table with infinity for uncomputed states.
        dp = [[inf] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 0  # Base case: no robots and no factories means zero cost.

        # Step 3: Fill DP table
        for j in range(1, m + 1):  # Process each factory
            position, limit = factory[j - 1]  # Factory's position and repair limit

            # Track cumulative costs for assigning robots to the current factory.
            cost_accum = [0] * (n + 1)
            for i in range(1, n + 1):
                cost_accum[i] = cost_accum[i - 1] + abs(robot[i - 1] - position)

            for i in range(n + 1):  # Process each subset of robots
                dp[i][j] = dp[i][j - 1]  # Case when no robots are assigned to this factory
                for k in range(1, min(limit, i) + 1):  # Assign up to `limit` robots to this factory
                    dp[i][j] = min(dp[i][j], dp[i - k][j - 1] + cost_accum[i] - cost_accum[i - k])

        # Final result: the minimum cost to repair all robots using all factories.
        return dp[n][m]


# Time Complexity
# Sorting the robot and factory arrays takes O(nlogn+mlogm).
# Filling the DP table requires O(n×m×L), where L is the repair limit for each factory.
# Thus, the total complexity is O(nlogn+mlogm+n×m×L).

# Space Complexity: O(n×m) due to the DP table.