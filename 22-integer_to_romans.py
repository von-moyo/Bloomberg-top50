# integer to roman
class Solution:
    def intToRoman(self, num: int) -> str:
        # Define the Roman numerals in descending order with corresponding values
        values = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]
        
        result = []
        
        # Iterate over the values and symbols
        for value, symbol in values:
            while num >= value:  # While the number is large enough to subtract the value
                result.append(symbol)  # Add the Roman symbol
                num -= value  # Subtract the value from num
        
        return ''.join(result)

# Time Complexity: O(log(num))
# Space Complexity: O(1)