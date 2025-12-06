# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        prev = None

        # Create gap
        slow = head
        fast = head
        counter = 0

        while counter < n:
            fast = fast.next
            counter += 1

        prev = None
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next

        # Removing the head case
        if not prev: 
            return head.next
        prev.next = slow.next
        return head
