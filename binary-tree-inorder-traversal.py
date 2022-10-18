# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#     Recursion Top Down
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        return res
        
#   Recursion bottom up
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(root):
            if root is None:
                return []
            res = inorder(root.left)
            res.append(root.val)
            res.extend(inorder(root.right))
            return ans
        return inorder(root)

#   one liner - elegant
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(root):
            return  inorder(root.left) + [root.val] + inorder(root.right) if root else []
        return inorder(root)
    
#   Iterative
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res

#   Morris
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        while root:
            if root.left is None:
                res.append(root.val)
                root = root.right
            else:
                temp = root.left
                while temp.right and temp.right != root:
                    temp = temp.right
                if temp.right == root:
                    temp.right = None
                    res.append(root.val)
                    root = root.right
                else:
                    temp.right = root
                    root = root.left
        return res
                
