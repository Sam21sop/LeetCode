class Solution:
    def generate(self, numRows):
        triangle = []
        for i in range(numRows):
            row = [1] * (i + 1)
            if i > 1:
                for j in range(1, i):
                    row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            triangle.append(row)
        return triangle
    

if __name__ == '__main__':
    numRows = 5
    obj = Solution()
    res = obj.generate(numRows)
    print(res)
    # for lst in res:
    #     print(lst) # , end=', ')