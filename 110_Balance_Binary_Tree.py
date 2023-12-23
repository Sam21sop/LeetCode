class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root):
        return self.checkHeight(root)
    

    def checkHeight(self, root):
        if not root:
            return 0
        
        # Check the height of left and right subtree 
        left_height = self.checkHeight(root.left)
        right_height = self.checkHeight(root.right)

        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1
        
        return 1 + max(left_height, right_height)
    


if __name__ == '__main__':
    pass