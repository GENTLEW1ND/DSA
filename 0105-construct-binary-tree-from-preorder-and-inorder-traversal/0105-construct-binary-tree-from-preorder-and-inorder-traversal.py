# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        inorderMap = {}

        for i in range(len(inorder)):
            inorderMap[inorder[i]] = i

        self.preindex = 0

        def build(left, right):

            if left > right:
                return None

            
            rootval = preorder[self.preindex]

            self.preindex += 1

            root = TreeNode(rootval)

            mid = inorderMap[rootval]

            root.left = build(left, mid-1)
            root.right = build(mid+1, right)

            return root

        return build(0, len(inorder) - 1)