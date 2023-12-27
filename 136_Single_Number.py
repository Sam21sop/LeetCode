class Solution:
    def singleNumber(self, nums:list[int]) -> int:
        ''' XORing a number with itself results in 0, and XORing any number with 0 results in the number itself '''
        result = 0
        for num in nums:
            result = result ^ num
        return result
    

if __name__ == '__main__':
    nums = [2,2,1]
    obj = Solution()
    res = obj.singleNumber(nums)
    print(res)