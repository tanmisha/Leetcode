# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if (p and q is not None):
            return p.val==q.val and Solution.isSameTree(self,p.left,q.left) and Solution.isSameTree(self,p.right,q.right)
        return False
        