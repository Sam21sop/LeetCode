# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p, q) -> bool:
        # if both node are the None they are same 
        if not p and not q:
            return True
        
        # if anyone is None then they are not same 
        if not p or not q:
            return False
        
        # Check the value and recursive call for left and right
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    


if __name__ == '__main__':
    pass        