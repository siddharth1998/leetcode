# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self):
        import heapq
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        lister = [(node3.val, node3),(node1.val,node1),(node2.val,node2)]
        
        heapq.heapify(lister)
        print(lister)

x = Solution()
x.mergeKLists()