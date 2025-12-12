# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.counter = 0 
        self.res = None
        self.k = k
        self.in_order(root)
        return self.res

    def in_order(self,root):
        if not root or self.res :
            return None
        self.in_order(root.left)
        self.counter +=1
        if self.counter == self.k :
            self.res = root.val
            return None
        self.in_order(root.right)

            