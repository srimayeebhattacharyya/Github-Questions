# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root)!=-1
    def height(self,node:TreeNode)->int:
        if not node:
            return 0
        leftheight=self.height(node.left)
        if leftheight==-1:
            return -1
        rightheight=self.height(node.right)
        if rightheight==-1:
            return -1
        if abs(leftheight - rightheight) > 1:
            return -1
        return max(leftheight, rightheight) + 1