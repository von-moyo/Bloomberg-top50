# length of longest substring

def lengthOfLongestSubstring(s: str) -> int:
    # Initialize variables
    char_map = {}  # To store the most recent index of each character
    left = 0       # Left pointer of the window
    max_len = 0    # To track the maximum length of the substring
    
    # Iterate over the string with the right pointer
    for right in range(len(s)):
        # If the character is already in the map and its index is greater than or equal to the left pointer
        if s[right] in char_map and char_map[s[right]] >= left:
            # Move the left pointer to the right of the previous occurrence of the character
            left = char_map[s[right]] + 1
        
        # Update the most recent index of the current character
        char_map[s[right]] = right
        
        # Update the maximum length of the window
        max_len = max(max_len, right - left + 1)
    
    return max_len

# Time Complexity: O(n)
# Space Complexity: O(k)