# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_ancestors = self.DFS(root, p)
        q_ancestors = self.DFS(root, q)
        res = None
        for i in range(len(p_ancestors)):
            for j in range(len(q_ancestors)):
                if p_ancestors[i] == q_ancestors[j] and not res:
                    res = p_ancestors[i]
                    break
        return TreeNode(res)

    def DFS(self, root, target):
        if root.val == target.val:
            return [root.val]
        res_l, res_r = [], []
        if root.left:
            res_l = self.DFS(root.left, target)
            if res_l:
                res_l.append(root.val)
        if root.right:
            res_r = self.DFS(root.right, target)
            if res_r:
                res_r.append(root.val)
        
        if res_l:
            return res_l
        else:
            return res_r
        
            