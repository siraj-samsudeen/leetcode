# All Nodes Distance K in Binary Tree - LeetCode
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def get_path(root, target, result):
            if root is None:
                return False
            
            if root == target:
                result.append(root)
                return True
            
            if get_path(root.left, target, result) or get_path(root.right, target, result):
                result.append(root)
                return True
            else:
                return False

        def nodes_at_distance(root, k):
            if root is None or k < 0: return []
            if k == 0: 
                return [root.val]
            
            res = nodes_at_distance(root.left, k-1)
            res += nodes_at_distance(root.right, k-1)
            return res

#         first find the nodes from the target downwards
        ans = nodes_at_distance(target, k)
        k-= 1

#         call get_path to populate the path to the target
        path = []
        get_path(root, target, path)

        for i in range(1, len(path)):
            if k == 0:
                ans.append(path[i].val)
            if path[i].left == path[i-1]:
                ans += nodes_at_distance(path[i].right, k-1)
            else:
                ans += nodes_at_distance(path[i].left, k-1)
            k -=1
        
        return ans