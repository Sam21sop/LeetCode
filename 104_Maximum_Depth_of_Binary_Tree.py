class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None
        

class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    

if __name__ == '__main__':
    pass