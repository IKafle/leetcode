from typing import List
class Solution:
    """
    Time complexity: O(nlogn)
    log n = dividing an array (binary search)
    n = merging an array back (using two pointers) 
    
    Space complexity : O(n)
    """
    def mergeSort(self, arr:List[int]):
        self.ms(arr, 0, len(arr)-1)


    def ms(self, arr:List[int], low:int, high:int):

        #Base case.
        # Return when low and high pointers meet (No further division is possible. i.e, reached the 
        # end of the recursion tree OR low and high points to a single item in the recursion tree.)
        if low == high: return
    
        mid : int = (low + high) //2
        self.ms(arr, low, mid)
        self.ms(arr, mid + 1 ,high)
        self.merge(arr, low, mid, high)

    def merge(self, arr:List[int], low:int, mid:int, high:int):
        left = low
        right = mid + 1

        sortedArray : List[int] = []

        # sort using two pointers
        while(left <= mid and right <= high):

            if(arr[left] <= arr[right]):
                sortedArray.append(arr[left])
                left += 1
            else:
                sortedArray.append(arr[right])
                right += 1
        
        # Append the remaining elements from left array if any elements left
        while(left <= mid):
            sortedArray.append(arr[left])
            left += 1

        # Append the remaining elements from right array if any elements left
        while(right <= high):
            sortedArray.append(arr[right])
            right += 1

        # Transferred the element from temporary Array to an original array
        i = low
        while i <= high :
            arr[i] = sortedArray[i - low]  # We will have index out of range if we do not use this condition.
            i += 1


if __name__ == "__main__":
    arr:List[int] = [3,1,2,4,1,5,6,2,4]
    Solution().mergeSort(arr)
    print(arr)