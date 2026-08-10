# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    interval = [-float('inf'), float('inf')]
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res_left = True
        res_right = True
        if root.left:
            temp = self.interval[1]
            self.interval[1] = root.val
            res_left = self.isValidBST(root.left)
            self.interval[1] = temp
        if root.right:
            temp = self.interval[0]
            self.interval[0] = root.val
            res_right = self.isValidBST(root.right)
            self.interval[0] = temp
        return res_left and res_right and (root.val > self.interval[0] and root.val < self.interval[1])

