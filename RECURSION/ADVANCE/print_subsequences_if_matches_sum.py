"""
Print all subsequence of an array which sums to k.
Do not use any global variables

if array = [1,2,1]
k = 2

subquences = [1,1], [2]

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

    def printSubsequences(self, num:List[int], k:int):
        n : int = len(num)
        stack : List[int]  = []
        sum = 0
        self.subsequences(num,k ,stack, n, 0, sum)

    
    def subsequences(self, num:List[int], k:int, ds:List[int] , length : int, index : int, sum : int):
        
        if length == index:

            if (sum == k):
                print(ds)

            return

        ds.append(num[index])
        sum += num[index]
        self.subsequences(num, k , ds, length, index + 1, sum)

        ds.pop()
        sum -= num[index]
        self.subsequences(num, k , ds, length, index + 1, sum)


if __name__ == "__main__":
    num:List[int] = [1,2,1]
    k:int =  2
    Solution().printSubsequences(num, k)

