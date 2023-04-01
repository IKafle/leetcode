"""
58. Length of Last Word

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
"""

class Solution:
    """
    TC : split() method splits the string s into a list of substrings based on whitespace characters.
    This operation takes O(n) time.
    SC : O(1)
    """
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])



if __name__=="__main__":
    string : str ="   fly me   to   the moon  "
    length: int = Solution().lengthOfLastWord(string)
    print(length)