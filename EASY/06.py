"""
Merge Two Sorted Lists:

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 
Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

"""

from typing import Optional
import sys
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
     
        # Initialize two pointers to the heads of both the lists.
        p : Optional[ListNode] = list1 # Pointer to the current node in list1
        q : Optional[ListNode] = list2 # Pointer to the current node in list2

        # Handle case where one or both input lists are empty
        if not p: return q # If list1 is None or empty, return list2
        if not q: return p # If list2 is None or empty, return list1

        # Create a dummy head node for the sorted merged list
        sorted = ListNode(~sys.maxsize) # Assign a dummy node with a very small -ve value.
                                        # A bitwise complement of the maximum integer value

        # Initialize a variable to keep track of the head of the sorted merged list
        new_head : Optional[ListNode] = None # Pointer to the head of the merged list

         # Determine which node should come first in the merged list (Node with smallest value )
        if p.val <= q.val:
            sorted = p # Set the dummy node to the first node of list1
            p = sorted.next # When dummy points to p, move P to the next node in list1
        else:
            sorted = q # Set the dummy node to the first node of list2
            q = sorted.next # When dummy points to q, move q to the next node in list2

         # Set the head of the sorted merged list
        new_head = sorted # Set the head of the merged list to the first node in the sorted list

        # Merge the rest of the nodes from both input lists
        while p and q:

            # Compare the values of the current nodes in both input lists
            if p.val <= q.val:
                # Add the current node from list1 to the end of the sorted merged list
                sorted.next = p # Set the next node in the merged list to the current node in list1
                sorted = p # Move the dummy node to the current node in list1
                p = sorted.next # Move to the next node in list1
            else:
                # Add the current node from list2 to the end of the sorted merged list
                sorted.next = q # Set the next node in the merged list to the current node in list2
                sorted = q # Move the dummy node to the current node in list2
                q = sorted.next # Move to the next node in list2

        # Add any remaining nodes from list1 or list2 to the end of the sorted merged list
        if p == None : sorted.next = q # If list1 is exhausted, add the rest of list2 to the end of the merged list
        if q == None : sorted.next = p # If list2 is exhausted, add the rest of list1 to the end of the merged list

        # Return the head of the sorted merged list
        return new_head



        
if __name__ == "__main__":

    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))

    s = Solution()

    merged_list = s.mergeTwoLists(list1, list2)
    while merged_list:
        print(merged_list.val, end=' ')
        merged_list = merged_list.next
        print()        
