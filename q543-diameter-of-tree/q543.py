# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0 

        def maxDepth(root):
            if root is None:
                return 0 
            left = maxDepth(root.left)
            right = maxDepth(root.right)
            self.max_diameter = max(self.max_diameter, left+right)
            return 1 + max(left,right)
        maxDepth(root)
        # def maximizer(left,right):
        #     if left is None and right is None:
        #         return 0 
        #     left = maxDepth(left)
        #     right = maxDepth(right)
        #     return max(left+right, maximizer(left.left, right.right))
        # max_path = maximizer(root.left, root.right)

        return self.max_diameter