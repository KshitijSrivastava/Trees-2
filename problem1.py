## Problem1 
#(https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0 or len(postorder) == 0:
            return None
        #print("in = ", inorder, "post = ", postorder)
        
        n = len(postorder)                      #find the length of the postorder arr
        node = TreeNode(postorder[n-1])         #make last node of postorder as roots
        
        index = inorder.index( postorder[n-1] ) #find index of the root in inorder
        
        #for node's left pass the inorder array to the left of root in the array
        node.left = self.buildTree(inorder[:index], postorder[:index])
        #for node's right pass the inorder array to the right of root in the array
        node.right = self.buildTree(inorder[index+1:], postorder[index:n-1])
        
        return node