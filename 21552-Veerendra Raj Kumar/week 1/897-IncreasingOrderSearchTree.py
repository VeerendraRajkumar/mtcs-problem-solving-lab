# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(head):
            if head:
                inorder(head.left)
                head.left = None
                self.node.right = head
                self.node = head
                inorder(head.right)
        ibst = self.node = TreeNode()
        inorder(root)
        return ibst.right