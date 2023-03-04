"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""
from typing import List 
class Solution:

    # Bruteforce solution
    def twoSumBruteforceSolution(self,nums: List[int], target: int) -> List[int]:
        length : int = len(nums)
        start : int = 0  # Set start pointer to first index of array
        end : int = length - 1  # Set end pointer to last index of array
        
        for i in range(0,length,1):
            start = i  # Move forward the start pointer by 1.
            while start < end: # Terminate loop if the end pointer meets start pointer.
                sum = nums[start] + nums[end]

                if sum == target:
                    print(f"Target Found At Indices :  [{start}, {end}]")
                    return [start, end]

                end = end -1  # Move backward the end pointer by 1.

            end = length - 1 # Reset the end pointer when the inner loop finishes.

    # Optimized solution
    def twoSum(self, nums, target):
        item_index_map = {} # Initialize a dict
        for index in range(0,len(nums),1):
            difference = target - nums[index]  # Check the difference between target and array item
            if difference in item_index_map:   # Check if difference exists in the dict
                return [item_index_map[difference],index]  # Return the two array indices.
            item_index_map[nums[index]] = index # Push current array item and its index to dict.
       


if __name__ == "__main__":

    print(Solution().twoSumOptimize([2,3,4,7,1], 5))