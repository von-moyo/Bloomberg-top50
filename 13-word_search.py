class Solution:
    def exist(self, board, word):
        def backtrack(i, j, k):
            if k == len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
                return False
            
            temp = board[i][j]
            board[i][j] = ''
            
            if backtrack(i+1, j, k+1) or backtrack(i-1, j, k+1) or backtrack(i, j+1, k+1) or backtrack(i, j-1, k+1):
                return True
            
            board[i][j] = temp
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
        return False
    

# Approach
# 1. Implement a recursive function backtrack that takes the current position (i, j) in the grid and the current index k of the word.
# 2.Base cases:
# If k equals the length of the word, return True, indicating that the word has been found.
# If the current position (i, j) is out of the grid boundaries or the character at (i, j) does not match the character at index k of the word, return False.
# 3.Mark the current cell as visited by changing its value or marking it as empty.
# 4. Recursively explore all four directions (up, down, left, right) by calling backtrack with updated positions (i+1, j), (i-1, j), (i, j+1), and (i, j-1).
# 5.If any recursive call returns True, indicating that the word has been found, return True.
# 6. If none of the recursive calls returns True, reset the current cell to its original value and return False.
# 7. Iterate through all cells in the grid and call the backtrack function for each cell. If any call returns True, return True, indicating that the word exists in the grid. Otherwise, return False.


# Time complexity:
# O(m∗n∗4^l) where m and n are the dimensions of the grid and l is the length of the word. The 4^l factor represents the maximum number of recursive calls we may have to make for each starting cell.
# Space complexity:
# O(l), where l is the length of the word. The space complexity is primarily due to the recursive stack depth during the DFS traversal.