class Solution:
    def hasPathSum(self, root, targetSum):
        # if root os None return False
        if not root:
            return False
        
        #check the current node is leaf
        if not root.left and not root.right:
            # if current node is node then check its value to tragetSum
            return root.val == targetSum
        
        #recursive call for left and right subtree
        # return true if there is path either subtree
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)


if __name__ == '__main__':
    pass 