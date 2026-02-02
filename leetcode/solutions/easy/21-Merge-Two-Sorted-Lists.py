'''
LeetCode #21: Merge Two Sorted Lists  
Date: January 15, 2026  
Difficulty: Easy  
Pattern: Two Pointers / Merge Pattern  
Time Complexity: O(n + m)  
Space Complexity: O(1)  

Problem:  
Given two sorted linked lists list1 and list2,  
merge them into one sorted linked list and return its head.  

Approach:  
Use a dummy node to simplify handling of the result list.  
Set a pointer current to the dummy node.  
While both lists are not empty:  
- Compare list1.val and list2.val.  
- Attach the smaller node to current.next.  
- Move the pointer in the chosen list forward.  
- Move current forward.  
After the loop, attach the remaining nodes from the non-empty list.  
Return dummy.next as the head of the merged list.  
'''
• explanation
• code

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(-1)  # fake starting node
        current = dummy

        while list1 and list2:  # while both lists are not empty
            if list1.val <= list2.val:
                current.next = list1  # take node from list1
                list1 = list1.next    # move list1 forward
            else:
                current.next = list2  # take node from list2
                list2 = list2.next    # move list2 forward
            current = current.next    # move current forward

        # append the remaining nodes (if any)
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return dummy.next  # return merged list starting after dummy
