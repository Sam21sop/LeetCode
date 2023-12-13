class Solution:
    def _helperReverse(self, number:int) -> int:
        rev_num = 0
        while number != 0:
            digit = number % 10
            rev_num = rev_num * 10 + digit
            number = number // 10
        return rev_num

    def isPalindrome(self, x: int) -> bool:
        if self._helperReverse(x) == x:
            return True
        else:
            return False


if __name__ == '__main__':
    num = 121
    obj = Solution()
    # print(obj._helperReverse(num))
    print(obj.isPalindrome(num))

