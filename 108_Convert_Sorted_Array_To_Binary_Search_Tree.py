class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums:list[int]):
        if not nums:
            return 
        
        # Find the middle element
        mid = len(nums) // 2

        # Create Root with the middle element
        root = TreeNode(nums[mid])

        # Recursively create left subtree and right subtree
        root.left = self.sortedArrayToBST(nums[ : mid])
        root.right = self.sortedArrayToBST(nums[mid + 1: ])

        return root
    

    def inorderTraversal(self, root):
        if not root:
            return
        self.inorderTraversal(root.left)
        print(root.val, end=' ')
        self.inorderTraversal(root.right)


if __name__ == '__main__':
    sorted_arr = [-10,-3,0,5,9]
    obj = Solution()
    root = obj.sortedArrayToBST(sorted_arr)
    obj.inorderTraversal(root)      # You will get same output