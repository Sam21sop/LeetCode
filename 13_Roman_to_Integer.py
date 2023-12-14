class Solution:
    symbols = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }


    def romanToInt(self, s: str) -> int:
        pass



if __name__ == '__main__':
    input_str = input()
    obj = Solution()
    print(obj.romanToInt(input_str))