"""
Intuition:
To achieve O(log (m + n)) time complexity, we use a binary search approach on the smaller of the two arrays. We partition both arrays such that the elements on the left side of the partition in both arrays combined are less than or equal to those on the right side. The median can then be found based on the maximum element on the left and the minimum element on the right.

Time Complexity: O(log(min(m, n))), where m and n are the lengths of the two arrays.
Space Complexity: O(1), as we use a constant amount of extra space.
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array to optimize binary search
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            partition1 = (left + right) // 2
            partition2 = (m + n + 1) // 2 - partition1

            # Edge cases for when partition is at the boundary
            max_left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            min_right1 = float('inf') if partition1 == m else nums1[partition1]
            
            max_left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            min_right2 = float('inf') if partition2 == n else nums2[partition2]

            # Check if we have found the correct partition
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                # If total length is even
                if (m + n) % 2 == 0:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
                # If total length is odd
                else:
                    return max(max_left1, max_left2)
            # Adjust binary search range
            elif max_left1 > min_right2:
                right = partition1 - 1
            else:
                left = partition1 + 1

# Time Complexity: O(log(min(m, n))), where m and n are the lengths of the two arrays.
# Space Complexity: O(1), as we use a constant amount of extra space.