"""
Print the subsequence of an array.

if array = [3,1,2]

subquences = [3,1,2], [3,1] , [3,2], [3] , [1,2], [1], [2] , []

"""
from typing import List
class Solution:

    """
    data structure used = stack (array as an stack)
    Time complexity: O(2^n) 
    - The program generates all possible subsequences of the input list by recursively
    branching into two cases at each index: either the element at that index is included 
    in the subsequence or it is not. This leads to a binary tree of 2^n possible paths, 
    and the program explores each path exactly once

    Space complexity : O(n)
    - The maximum size of ds in the program is equal to the maximum depth of the recursive call stack,
    which is equal to n (the length of the input list nums)
    """
    def printSubsequences(self, num:List[int]):
        self.nums = num
        self.subsequences(0, [])

    def subsequences(self, index:int, ds:List[int]):

        # Base Case.
        # If we have reached the end of the input list `nums`, we have constructed a valid subsequence.
        if index == len(self.nums):
            print(ds)
            return

        # Take the element at the current index
        ds.append(self.nums[index]) # push into the stack
        # make a recursive call.
        self.subsequences(index + 1 , ds)
        # Not take the element at the current index
        ds.pop() # pop from the stack
        # make a recursive call.
        self.subsequences(index + 1, ds)


if __name__ == "__main__":
    Solution().printSubsequences([3,1,2])
