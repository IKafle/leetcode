"""
27. Remove Element

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, 
you must instead have the result be placed in the first part of the array nums.
More formally, if there are k elements after removing the duplicates, then the
first k elements of nums should hold the final result. It does not matter what
you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input
array in-place with O(1) extra memory.

Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums 
containing 0, 0, 1, 3, and 4.

Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""

from typing import List
class Solution:
    """
    Time complexity: O(n) 
    Space complexity : O(1)
    """
    def removeElement(self, nums: List[int], val: int) -> int:

        # Initialize two pointers
        p: int = 0
        q: int = len(nums) - 1

        # Iterate until two pointers meet
        while p <= q :

            if nums[p] == val :

                if nums[q] == val:
                    q -= 1
                    continue

                nums[p] , nums[q]  = nums[q] , nums[p]
                p += 1
                q -= 1
                continue

            p += 1

        # Special case : when all the elements in the list are same.
        # We only move the right pointers by 1 towards left. The left pointer is not moved.
        if p == 0 : return 0
        return p


if __name__ == "__main__":
    Solution().removeElement([3,2,2,3], 3)
