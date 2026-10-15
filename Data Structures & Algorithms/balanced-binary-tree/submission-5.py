# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        self.height(root)
        return self.res
        
    def height(self, curr):
        if not curr:
            return 0
        left, right = 0, 0
        if curr.left:
            left = self.height(curr.left)
        if curr.right:
            right = self.height(curr.right)

        self.res = abs(left - right) <= 1 and self.res

        return max(left, right) + 1