class Solution:
    def removeDuplicates(self, nums:list[int]) -> int:
        if not nums:
            return []
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)
    

if __name__ == '__main__':
    sorted_array = [1, 1, 2]
    obj = Solution()
    res = obj.removeDuplicates(sorted_array)
    print(res)