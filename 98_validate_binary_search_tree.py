# https://leetcode.com/problems/validate-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def withinRange(node, min, max):
            if node is None: return True
            if node.val < min or node.val > max:
                return False
            return withinRange(node.left, min, node.val-1) \
                and withinRange(node.right, node.val+1, max)

        return withinRange(root, float('-inf'), float('inf'))
        