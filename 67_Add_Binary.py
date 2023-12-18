class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        # Ensure the length of both the string
        # Making them same by padding zeroes
        a = a.zfill(max(len(a), len(b)))
        b = b.zfill(max(len(a), len(b)))

        
        for i in range(len(a) - 1, -1, -1):             # Iterate through the string from right to left 
            bit_sum = int(a[i]) + int(b[i]) + carry
            result.insert(0, str(bit_sum % 2))          # Insert the current bit at the beginning
            carry = bit_sum // 2
        if carry:
            result.insert(0, str(carry))
        return ''.join(result)
    

if __name__ == '__main__':
    a = '1010'
    b = '1011'
    obj = Solution()
    print(obj.addBinary(a, b))
