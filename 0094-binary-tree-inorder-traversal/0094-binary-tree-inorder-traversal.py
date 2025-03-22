# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def traverse(root):
            if root == None:
                return ans 
            if root.left != None:
                traverse(root.left)
            ans.append(root.val)
            if root.right != None:
                traverse(root.right)

        traverse(root)
        return ans