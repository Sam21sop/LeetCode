class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root) -> bool:
        if not root:
            return
        return self.isMirror(root.left, root.right)
    

    def isMirror(self, left, right):
        if not left and not right:
            return True
        
        if not left and not right:
            return False
        
        return left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right,left)
    

if __name__ == '__main__':
    pass