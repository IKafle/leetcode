"""
28.Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first
occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
"""

class Solution:
    """
    Time complexity: O(m * n): 
       if m is the length of needle and n is the length of haystack.
       The python function find() uses the boyer-moore-horspool Algorithm which finds all
       the occurences of a substring in a string. 
    Space complexity : O(1)
    """
    def strStr(self, haystack: str, needle: str) -> int:

        if not needle:
            return -1

        return haystack.find(needle)
    
if __name__ == "__main__":
    haystack : str = 'leetcode'
    needle : str  = 'leeto'
    print(Solution().strStr(haystack, needle))