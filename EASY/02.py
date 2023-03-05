"""
Given an integer n, return true if n is a palindrome , and false otherwise.

Enample 1:
Input: n = 121
Output: true
Enplanation: 121 reads as 121 from left to right and from right to left.

Enample 2:
Input: n = -121
Output: false
Enplanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Enample 3:
Input: n = 10
Output: false
Enplanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""
class Solution:
    """
    Time complexity: O(logn)
    - The for loop iterates over each digit of n, which takes O(log n) time in the worst case.

    Space complexity : O(log n)
    """
    #Bruteforce Solution
    def isPalindrome(self, n: int) -> bool:
        reverse : int = 0
        num : int = n
        for _ in range(0, len(str(n)),1):
            digit : int = num % 10
            num = int(num / 10)            
            power:int = 0 if num == 0 else len(str(num))
            reverse = reverse + digit * (10 ** power)

        return reverse == n


    """
    Time complexity: O(logn)
    - The number of iterations is equal to the number of digits in x

    Space complexity : O(1)
    - It uses only a constant amount of extra space for storing the variables rev, 
      num and a few other integers
    """
    #Optimal Solution
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num = x
        rev = 0
        while num > 0:
            rev = rev * 10 + num % 10
            num = num // 10
        return x == rev


    # Pythonic way
    def isPalindrome(self, n: int) -> bool:
        return str(n) == str(n)[::-1]

if __name__=="__main__":
    print(Solution().isPalindrome(313))