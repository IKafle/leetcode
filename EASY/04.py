"""
Longest Common Prefix : 

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Python Slicing example : https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types/

"""
from typing import List
class Solution:
    """
    Technique Used : HORIZONLAL SCANNING

    Time complexity: O(N*M) 
    - Here : N = number of items in the array
             M = length of the longest item (string) in the array.
    - Total number of comparisons = (N-1)M
    - In the worst case scenario, every character of each string is compared with the 
      corresponding character of the prefix.

    Space complexity : O(1)
    - Constant amount of extra space is used to store the prefix, the loop variable i, and the loop conditions
      regardless of the input size. 
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        prefix = strs[0]
        for index in range(1, len(strs) , 1):
            while strs[index].find(prefix) !=0:
                prefix = prefix[0:len(prefix)-1] #Remove a character on each iteration until we have common character/s on both the strings

                if not prefix:
                    return prefix
        
        return prefix

        
if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    print(Solution().longestCommonPrefix(strs))