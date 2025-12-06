from typing import Optional, List
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):Optional
        self.val = val
        self.next = next
        
        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]):
        mHeap = []

        for idx, node in enumerate(lists):
            if node:
                heapq.heappush(mHeap,(node.val, idx, node))

        prev = ListNode(0)
        head = prev
        while(mHeap):
            val, idx, node = heapq.heappop(mHeap)
            prev.next = node
            prev = prev.next

            if node.next : 
                nextNode = node.next
                heapq.heappush(mHeap, (nextNode.val, idx , nextNode))
        return head.next
