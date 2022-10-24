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
        def get_path(root, target, path):
            if root is None:
                return False
            
            # if the root matches the target
            # OR if there is a match on the left or right subtree
            if root == target or get_path(root.left, target, path) or get_path(root.right, target, path):
                path.append(root)
                return True
            else:
                return False
            
        def nodes_below_at_distance(root, k):
            if root is None or k < 0: return []
            if k == 0:return [root.val]
            
            return nodes_below_at_distance(root.left, k-1) + nodes_below_at_distance(root.right, k-1)

        # first find the nodes from the target downwards
        ans = nodes_below_at_distance(target, k)
        k -= 1

        path = []
        get_path(root, target, path)
        
        for i in range(1, len(path)):
            current = path[i]
            prev = path[i-1]
            if k == 0:
                ans.append(current.val)
            if current.left == prev:
                ans += nodes_below_at_distance(current.right, k-1)
            else:
                ans += nodes_below_at_distance(current.left, k-1)
            k -=1
        return ans