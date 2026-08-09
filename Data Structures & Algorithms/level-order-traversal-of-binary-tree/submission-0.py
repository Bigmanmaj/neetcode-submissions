# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            nums = []
            lower_nodes = []
            for node in queue:
                nums.append(node.val)
                if node.left:
                    lower_nodes.append(node.left)
                if node.right:
                    lower_nodes.append(node.right)
            queue = lower_nodes
            res.append(nums)
        return res