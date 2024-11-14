class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        profit = 0
        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - prices[start])
            if prices[i] < prices[start]:
                start = i
        return profit
    
# Time Complexity = O(n)
# Space Complexity = O(1)