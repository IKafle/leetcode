"""
Print the subset sum.
The resulted sum should be in the sorted order.

if array = [2,1,3]

then , sum = [0,1,2,3,3,4,5,6]

TC : 2^n + 2^nlog(2^n)  [recursive solution + sorting (resulted sorted list = 2^n)]
SC : 2^n (ds contains the sum where number of elements = 2^n)
Note : there are 'N' indices and for each indices there are two choices : pick and not-pick
"""

from typing import List
class Solution:
    def findSubsetSum(self, arr:List[int]) -> List[List[int]] :
        ds : List[int] = []

        self.subsetSum(0, 0, arr, ds)

        return ds



    def subsetSum(self, index : int, sum : int, arr:List[int], ds:List[int]) -> None :
        
        #Base case
        if index == len(arr):
            # Add the sum to list when the current index > size of list.
            # Leaf of the recursion tree. (Analogy)
            ds.append(sum)
            return
        
        # Pick the element
        sum += arr[index]
        self.subsetSum(index + 1, sum, arr, ds)

        # Do-not pick the element
        sum -= arr[index]
        self.subsetSum(index+1, sum, arr, ds)





if __name__ == "__main__":
    arr:List[int] = [3,1,2]
    container: List[List[int]] = Solution().findSubsetSum(arr)
    container.sort()
    print(container)
