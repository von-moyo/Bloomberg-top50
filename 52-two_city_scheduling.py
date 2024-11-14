class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        cost = sorted(costs, key = lambda x: x[0] - x[1])
        total = 0
        n = len(cost) // 2

        for i in range(len(cost)):
            if i < n:
                total += cost[i][0]
            else:
                total += cost[i][1]

        return total
    
# time complexity = O(nlogn)
# space complexity = O(n)