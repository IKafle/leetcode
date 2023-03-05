"""
Given an integer x, return true if x is a palindrome , and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""
import math
class Solution:
    #Bruteforce Solution
    def isPalindrome(self, x: int) -> bool:
        sum : int = 0
        num : int = x
        for _ in range(0, len(str(x)),1):
            digit : int = num % 10
            num = int(num / 10)            
            power:int = 0 if num == 0 else len(str(num))
            sum = sum + digit * (10 ** power)

        return sum == x

if __name__=="__main__":
    print(Solution().isPalindrome(313))