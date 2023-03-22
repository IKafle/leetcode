
from typing import List
class Solution:

    def flattenSum(self, nums:List[list[int]]):
        
        self.flattenAndSum(0, len(nums),  nums, [])


    def flattenAndSum(self, index : int, n : int,  nums:List[List[int]], flattened:List[int]):
        
        #Base Case
        if (index == n):
            sum : int = 0

            for i in range(len(flattened)):
                sum += flattened[i]
            
            print(f"The flattened sum = {sum}")
            return

        flattened += nums[index]
        self.flattenAndSum(index + 1, n, nums, flattened)


if __name__ == "__main__":
    nums:List[List[int]] = [[1,2,3],[4,5],[6,7,8,9,10]]
    Solution().flattenSum(nums)