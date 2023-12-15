class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack
    
if __name__ == '__main__':
    obj = Solution()
    input_str = "()[]{}"
    res = obj.isValid(input_str)
    print(res)

    input_str = "(}"
    res = obj.isValid(input_str)
    print(res)