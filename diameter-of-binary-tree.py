# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root or (not root.right and not root.left):
            return 0
        self.ans = 1
        
        def depth(node):
            if not node:
                return 0
            
            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, L + R)
            return max(L, R) + 1
            
        depth(root)
        return self.ans
            
    
            
        
        
