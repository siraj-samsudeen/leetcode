# Serialize and Deserialize Binary Tree - LeetCode
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        que = deque()
        que.append(root)
        res = []
        
        while que:
            node = que.popleft()
            if node is None:
                res.append("")
                continue
            else:
                res.append(str(node.val))
            
            que.append(node.left)
            que.append(node.right)
        
        return ",".join(res)
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return

        a = data.split(",")
        que = deque()
        root = TreeNode(a[0])
        que.append(root)
        
        i = 1
        while que :
            node = que.popleft()
            if a[i] :
                node.left = TreeNode(a[i])
                que.append(node.left)
            i+= 1
            if a[i] :
                node.right = TreeNode(a[i])
                que.append(node.right)
            i+= 1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))