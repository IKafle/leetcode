from typing import List

class Solution:
    
    #BF: sort the array and run two pointers (i and j by 1 step from left)
    
    # TC : O(n)
    # SC : O(n)
    def containsDuplicate(self, nums:list[int]) -> bool:
        
        hashSet = set()
        for num in nums:
            
            if num in hashSet:
                return True
            
            hashSet.add(num)
            
        return False
    
    
    # TC : O(3n)
    # SC : O(n)
    def isAnagram(self, s: str, t: str) -> bool:
    
        dict = {}
        
        def populateForS():
            
            for char in s:
            
                if char in dict:
                    dict[char] += 1
                    continue
                
                dict[char] = 1
                    
        def removeFromT():
            
            for char in t:
                
                if char in dict:
                    dict[char] -= 1
                    continue

                break
        
        populateForS()
        removeFromT()

        for value in dict.values():
            if value !=0:
                return False

        return True

    # TC : O(n)
    # SC : O(n)
    def twoSum(nums: List[int], target: int) -> List[int]:
        cache = {}
        for index, num in enumerate(nums):
            secondNumber = target - num
            if secondNumber in cache:
                return [cache[secondNumber], index]
            cache[num] = index
        return [0, 0]


    if __name__ == '__main__':
        print(twoSum([3,4,5,6],7))

            
                    
                
                
            
        
        