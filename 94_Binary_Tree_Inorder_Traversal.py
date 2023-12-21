from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root) -> list[int]:
        result = []
        self._helperIorderRecursive(root, result)
        return result
    

    def _helperIorderRecursive(self, root, result):
        if root:
            self._helperIorderRecursive(root.left, result)
            result.append(root.val)
            self._helperIorderRecursive(root.right, result)


    def buildTree(self, level_order):
        if not level_order:
            return None
        root = TreeNode(level_order[0])
        queue = deque([root])
        i = 1
        while queue and i < len(level_order):
            current_node = queue.popleft()

            if level_order[i] is not None:
                current_node.left = TreeNode(level_order[i])
                queue.append(current_node.left)
            i += 1

            if level_order[i] is not None:
                current_node.right = TreeNode(level_order[i])
                queue.append(current_node.right)
            i += 1
        
        return root


if __name__ == '__main__':
    level_order = [1]
    obj = Solution()
    root = obj.buildTree(level_order) # buildTree function not work properly
    res = obj.inorderTraversal(root)
    print(res)