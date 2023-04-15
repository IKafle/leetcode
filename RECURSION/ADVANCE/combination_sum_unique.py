"""
Print all the unique combination of an array that matches the target sum.
Repeatation is not allowed and the subsequence should be unique (duplicate sub-sequences are not allowed).

if array = [2,1,1,2,1] , target = 4

combinations = [1,1,2], [2,2]

"""
from typing import List
class Solution:
    def findUniqueCombination(self, arr:List[int], target:int) -> List[List[int]] :
        container = []
        arr.sort()
        print(f" sorted array : {arr}")
        self.combinationSum(0, target, arr, container, [])

        return container


    def combinationSum(self, index, target, arr:List[int], container:List[List[int]], ds:List[int]) -> None :
        
        #Base case
        if target == 0:
            container.append([item for item in ds])
            return
        
        # We will only loop:  for i == index, i < len(arr) ; i++
        for i in range(index , len(arr)):
            if arr[i] > target: break
            # This is our 'Not Take' option
            if i > index and arr[i] == arr[i-1]: continue
    
            # 'Take' option : Perform the recursion
            # the item is removed from the ds once the recursion gets completed. 
            ds.append(arr[i])
            # On the recursion tree, the for loop iterates in branches from left to right. (Horizontally)
            # The recursive call causes the recursion tree grow from top to bottom. (Vertically) 
            self.combinationSum(i+1, target-arr[i], arr,container, ds)
            ds.pop()
            
        # 'Not take' option : We are not considering this option. 
        #  We will `continue` the loop and do nothing.





if __name__ == "__main__":
    arr:List[int] = [2,1,1,2,1]
    target = 4
    container: List[List[int]] = Solution().findUniqueCombination(arr,target)
    print(container)
