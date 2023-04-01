"""
Print all the combination of an array that matches the target sum.
Repeatation is allowed for any number of times.

if array = [2,3,6,7] , target = 7

combinations = [2, 2, 3], [7]

"""



from typing import List
class Solution:
    def findCombination(self, arr:List[int], target:int) -> List[List[int]] :
        container = []
        self.combinationSum(0, target, arr, container, [])

        return container


    def combinationSum(self, index, target, arr:List[int], container:List[List[int]], ds:List[int]) -> None :
        
        # Base Case:
        if index == len(arr):
            if target == 0:
                container.append([item for item in ds])

            return

        # Happy scenario.
        # 'Take' option will make the recursive call and it makes the recursion tree 
        #  naturally skewed towards the left. Once the recursion is complete, the item is 
        #  removed from the ds. 
        if arr[index] <= target:
            ds.append(arr[index])
            self.combinationSum(index, target-arr[index], arr,container, ds)
            ds.pop()
        
        # 'Not take' option will make the recursion tree more skewed towards the right.
        # Note that , we are not subtracting array items from the target.
        self.combinationSum(index + 1, target, arr, container, ds)




if __name__ == "__main__":
    arr:List[int] = [2,3,6,7]
    target = 7
    container: List[List[int]] = Solution().findCombination(arr,target)
    print(container)