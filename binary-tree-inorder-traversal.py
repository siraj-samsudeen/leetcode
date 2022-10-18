# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        ans = self.inorderTraversal(root.left)
        ans.append(root.val)
        ans.extend(self.inorderTraversal(root.right))
            
        return ans

    #     one liner - elegant
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(self, root):
            return  self.inorder(root.left) + [root.val] + self.inorder(root.right) if root else []
        return inorder(root)
    
    
    #     Top down
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            result.append(current_node.val)
            if current_node.right:
                traverse(current_node.right)
        if root:
            traverse(root)
        return result
    
    #     Just only one place to append to the list
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        
        inorder(root)
        return res
    
    #     Iterative Traversal
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorderIter(root):
            result = []
            stack = []
#             if the root is not null or if the stack is not empty
            while root or stack:
                if root:
                    stack.append(root)
                    root = root.left
                else:
                    root = stack.pop()
                    result.append(root.val)
                    root = root.right
            return result
            
        return inorderIter(root)

#     Morris Traversal
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorderMorris(root):
            result = []
            while root:
                if root.left is None:
                    result.append(root.val)
                    root = root.right
                else:
                    temp = root.left
                    while temp.right and temp.right != root:
                        temp = temp.right
                    if temp.right == root:
                        temp.right = None
                        result.append(root.val)
                        root = root.right
                    else:
                        temp.right = root
                        root = root.left
            return result
                            
        return inorderMorris(root)