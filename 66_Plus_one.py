class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # return [carry for carry in map(int, str(int(''.join(map(str, digits))) + 1))]  # list coprehensive
        n = len(digits)
        carry = 1  # Initialize carry to 1 as we are incrementing by one

        for i in range(n - 1, -1, -1):  # optimize it by iterating uptile we get last digit is 9
            total = digits[i] + carry
            digits[i] = total % 10
            carry = total // 10
            

        # If there is still a carry after the loop, insert it as a new most significant digit
        if carry:
            digits.insert(0, carry)

        return digits
    


if __name__ == '__main__':
    digits = [1, 9, 9]
    # digits.insert(-1, 1)
    # print(digits)
    obj = Solution()
    print(obj.plusOne(digits))