## Problem2 (https://leetcode.com/problems/sum-root-to-leaf-numbers/)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Time Complexity: O(N)
Space Complexity: O(1)
"""
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        total = 0
        arr = []
        def findSum(root, current):
            # if root is None, return
            if root is None:
                return
            
            #if its the last node
            if root.left is None and root.right is None:
                current = (current * 10) + root.val
                nonlocal total
                total += current
                return 
            
            #traverse both left and right trees
            findSum(root.left, (current * 10) + root.val )
            findSum(root.right, (current * 10) + root.val )
            
        findSum(root, 0)
        return total