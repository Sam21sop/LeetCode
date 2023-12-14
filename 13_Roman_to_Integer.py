class Solution:

    def romanToInt(self, s: str) -> int:
        symbols = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        count = 0
        index = 0
        while index < len(s):
            ch1 = symbols[s[index]]
            if index + 1 < len(s):
                ch2 = symbols[s[index + 1]]
                if ch1 >= ch2:
                    count += ch1
                    index += 1
                else:
                    count = count + ch2 - ch1
                    index += 2
            else:
                count += ch1
                index += 1
        return count



if __name__ == '__main__':
    input_str = input()
    obj = Solution()
    print(obj.romanToInt(input_str))