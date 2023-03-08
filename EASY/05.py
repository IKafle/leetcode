"""
Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

"""

from typing import List
class Solution:
    """
    Data Structure Used : Stack
    stack = []
    append() - push item into stack
    stack[size-1] - Get the most recently pushed item from the stack

    Time complexity: O(n) 
    -  the loop iterates over the string once, performing constant-time operations 
        (i.e., pushing, popping, or checking the top of the stack) at each character.

    Space complexity : O(n)
    - The size of the stack increases with the input size. 
    """
    def isValid(self, s: str) -> bool:

        if not s:
            return True

        # If the string begins with these characters, we will call it an invalid string
        invalids : List[str] = [')',']','}']
        stack : List[str] = []

        # For safety, we will push the first character into the stack
        stack.append(s[0])

        for i in range(1, len(s), 1):
            size = len(stack)
            
            # Check if we have invalid character once the stack is empty
            if size == 0 and s[i] in invalids:
                return False
            
            condition1 : bool = s[i] == ')' and stack[size-1] == '('
            condition2 : bool = s[i] == '}' and stack[size-1] == '{'
            condition3 : bool = s[i] == ']' and stack[size-1] == '['

            if any([condition1 , condition2 , condition3]):
                # Remove from stack if the incoming character is any opening parentheses
                # and its closing parentheses present on the TOS
                stack.pop() 
            else:
                # If the opening parentheses are not mached with TOS, keep pushing into the stack
                stack.append(s[i])
        
        # The string is valid if the stack is empty
        return len(stack) == 0
    

if __name__=='__main__':
    string:str = "(){}}{"
    print(Solution().isValid(string))