# Palindrome number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Convert the integer to a string
        s = str(x)
        left, right = 0, len(s) - 1

        # Compare digits from left and right until they meet in the middle
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True


# Time Complexity = O(n)
# Space Complexity = O(n)


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False
        
        # Single digit numbers are always palindromes
        if x < 10:
            return True
        
        # Reverse half of the number and compare
        original = x
        reversed_half = 0
        
        while original > reversed_half:
            reversed_half = reversed_half * 10 + original % 10
            original //= 10
        
        # If the number is odd, we can remove the middle digit
        return original == reversed_half or original == reversed_half // 10
    
# The main computational work occurs in the while loop, which reduces the
#  number of digits in original by one on each iteration. For an
#  integer x with d digits, the loop runs approximately 
# d/2 times because it processes half of the digits. Since 
# d is proportional to log10(x), the time complexity is:O(log 10 (x))

# Space Complexity = O(1)