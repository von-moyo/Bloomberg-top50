class Solution:
    def solution(self, A):
        n = len(A)
        
        # If the array has fewer than 2 elements, return 0 since no tiles can be placed.
        if n < 2:
            return 0
        
        # Step 1: Precompute the sum of adjacent pairs
        pair_sums = [A[i] + A[i+1] for i in range(n-1)]

        # Step 2: Initialize a DP table for up to 3 tiles
        # dp[i][j] = maximum sum with at most j tiles and up to the i-th element
        dp = [[0] * 4 for _ in range(n)]
        
        # Step 3: Fill the DP table
        for i in range(2, n):  # We can only place tiles starting from the 2nd element
            for j in range(1, 4):  # We only care about 1 to 3 tiles
                dp[i][j] = max(dp[i-1][j], dp[i-2][j-1] + pair_sums[i-1])
        
        # Step 4: The answer is the maximum sum with 3 tiles, considering all positions
        return max(dp[n-2][1], dp[n-2][2], dp[n-2][3])



# Time Complexity: O(N)
# Space Complexity: O(N)