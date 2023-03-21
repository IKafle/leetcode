"""
35. Search Insert Position

Given a sorted array of distinct integers and a target value, 
return the index if the target is found. If not, return the index 
where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 
Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
"""
from typing import List
class Solution:
    """
    Time complexity: O(log n) 
    - The program implements the binary search algorithm to search for a target
    element in a sorted list of integers

    Space complexity : O(1)
    - The program only uses a constant amount of extra space for storing the left, 
    right, and middle indices
    """
    def searchInsert(self, nums: List[int], target: int) -> int:
        left:int = 0
        right:int = len(nums)
        return self.binarySearch(left , right-1, nums, target)

    def binarySearch(self, left:int, right:int, nums:List[int] , target:int) ->int:

        middle : int = (left + right)//2

        # Base Case
        if left == right:
            
            if target > nums[middle]:
                return middle + 1
            
            return middle

        if (target > nums[middle]):
            left = middle + 1
        else:
            right = middle

        return self.binarySearch(left, right, nums , target)


if __name__ == "__main__":
    nums: List[int] = [1,3,5,6]
    target: int = 5
    print(Solution().searchInsert(nums, target))