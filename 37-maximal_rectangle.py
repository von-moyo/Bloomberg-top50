# maximal rectangle

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        rows = len(matrix)
        cols = len(matrix[0])
        heights = [0] * cols  # This will store the heights of the histogram bars
        max_area = 0

        for row in matrix:
            # Update histogram heights for this row
            for i in range(cols):
                if row[i] == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0

            # Calculate the largest rectangle area for the current histogram
            max_area = max(max_area, self.calculateMaxArea(heights))

        return max_area

    def calculateMaxArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)  # Add a 0 at the end to ensure we flush the stack at the end
        
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            
            stack.append(i)

        return max_area


# time: O(rows x cols)
# space: O(cols)