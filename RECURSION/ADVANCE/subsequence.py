"""
Print the subsequence of an array.

if array = [3,1,2]

subquences = [3,1,2], [3,1] , [3,2], [3] , [1,2], [1], [2] , []

"""
from typing import List
class Solution:
    def printSubsequences(self, num:List[int]):
        self.nums = num
        self.subsequences(0, [])

    def subsequences(self, index:int, ds:List[int]):
        if index == len(self.nums):
            print(ds)
            return
        
        ds.append(self.nums[index])
        self.subsequences(index + 1 , ds)
        ds.pop()
        self.subsequences(index + 1, ds)


if __name__ == "__main__":
    print(Solution().printSubsequences([3,1,2]))
