"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

"""
from typing import Dict, Tuple
class Solution:

    """
    Time complexity: O(n)
    - The program loops through the string "s" one character at a time, 
       and performs constant time operations (such as dictionary lookups 
       and addition/subtraction operations) on each character.

    Space complexity : O(1)
    - It uses a constant amount of additional space to store the dictionary, 
       rule list, accumulator, and loop index.
    - The size of these data structures does not depend on the length of the input string.
    """
    def romanToInt(self, s: str) -> int:
        roman_dict :Dict  = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }
        
        index : int = 0
        rule : Tuple[str] = ('IV', 'IX', 'XL', 'XC', 'CD', 'CM',)
        accumulator: int = 0
        length : int = len(s)
        # Run loop until the curent index equalize or exceeds the length of an string array. 
        while index < length:
            
            # Calculate and return the accumulator if the index points to the last item of an string array.
            # Special Case
            if index + 1 >= length:
                accumulator = accumulator + roman_dict[s[index]]
                return accumulator

            # Get the rule item based on the current and next index.
            chars = ''.join([s[index],s[index + 1]])

            # Check if current rule item is present in the rule List.
            if chars in rule:
                """
                Rule for calculation
                IV = V - I
                IX = X - I
                XL = L - x 
                XC = C - X
                CD = D - C
                CM = M - C
                """
                accumulator = accumulator + (roman_dict[s[index + 1]] - roman_dict[s[index]])
                # Apply the special rule performing the dictionary lookup and perform addition.
                # Increment the index by 2
                index = index + 2 
            else :
                 # Apply the simple addition peforming the dictionary lookup.
                 # Increment the index by 1
                accumulator = accumulator + roman_dict[s[index]]
                index = index + 1

        return accumulator


if __name__ == '__main__':
    print(Solution().romanToInt('MCMLXXXIX'))
