class Solution:
    def minDepth(self, root):
        # if tree is empty then depth is 0
        if not root:
            return 0
        
        # if node is leaf, the depth is 1
        if root.left is None and root.right is None:
            return 1
        
        # if left subtree is empty, Calculate right subtree
        if root.left is None:
            return 1 + self.minDepth(root.right)        # 1 for root node
        
        # if right subtree is empty, Calculate left subtree
        if root.right is None:
            return 1 + self.minDepth(root.left)
        
        # if node has both left and right children, calculate minnimum depth between them
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
    


if __name__ == '__main__':
    pass