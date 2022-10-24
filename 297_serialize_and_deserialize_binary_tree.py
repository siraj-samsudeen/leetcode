# Serialize and Deserialize Binary Tree - LeetCode
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
import queue
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
            current = que.popleft()
            if current:
                que.append(current.left)
                que.append(current.right)
                res.append(str(current.val))
            else:
                res.append("") #we append an empty string for null
        
        return ",".join(res)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
                
        data = data.split(",")
        
        root = TreeNode(data[0])
        i = 1
        
        que = deque()
        que.append(root)
        
        while que :
            current = que.popleft()
            if data[i] :
                current.left = TreeNode(data[i])
                que.append(current.left)
            i += 1
            if data[i] :
                current.right = TreeNode(data[i])
                que.append(current.right)
            i += 1

        return root
            
        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))