from math import log2, log10

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        new_num = (len(str(x)) + 1) // 2 
        new_num = float( 10 ** new_num)

        while int(new_num * new_num) > x:
            new_num = (new_num + (x / new_num)) / 2

        return int(new_num)

    

if __name__ == '__main__':
    x = 17
    obj = Solution()
    print(obj.mySqrt(x))

