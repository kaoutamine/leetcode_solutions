"""version 1 : recursive logic with minimum/maximum propagating down the tree"""
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, minimum, maximum):
            if not node:
                return True
            if node.val <= minimum:
                return False
            elif node.val >= maximum:
                return False
            
            return helper(node.left, minimum, node.val) and helper(node.right,node.val, maximum)

        return helper(root,float(-inf), float(inf))
        