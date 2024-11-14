class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l= 0 
        r = len(height) - 1
        while l < r:
            area = (r - l) * min(height[l], height[r])
            max_area = max(max_area, area)
            if height[r] > height[l]:
                l +=1 
            elif height[r] < height[l]:
                r -= 1
            else:
                l += 1
        return max_area


# Time Complexity: O(n), where n is the length of height
# Space Complexity: O(1) This approach uses a constant amount of extra space, only requiring variables for max_area, l, r, and area.