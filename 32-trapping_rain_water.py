# two-pointer technique. This approach is efficient because it only
# requires a single pass through the array, resulting in O(n) time
# complexity and O(1) extra space complexity.

# Problem Understanding:
# Each bar represents an elevation. The amount of water that a bar
# can trap depends on the height of the tallest bars to its left and
# right. The water above each bar is determined by the minimum of these 
# two heights (since water cannot be held higher than the shorter "wall" 
# on either side).

def trap(height: List[int]) -> int:
    if not height:
        return 0

    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water_trapped = 0

    while left < right:
        if left_max < right_max:
            # Calculate water at the left pointer
            left += 1
            left_max = max(left_max, height[left])
            water_trapped += max(0, left_max - height[left])
        else:
            # Calculate water at the right pointer
            right -= 1
            right_max = max(right_max, height[right])
            water_trapped += max(0, right_max - height[right])

    return water_trapped


# Time Complexity: O(n)
# Space Complexity: O(1)