from math import comb

class Solution:
    def getRow(self, rowIndex):
        ''' The Expansion of (a + b)^rowIndex '''
        row = []
        for i in range(rowIndex + 1):
            row.append(comb(rowIndex, i))
        return row
    

if __name__ == '__main__':
    rowIndex = 5
    obj = Solution()
    res = obj.getRow(rowIndex)
    print(res)