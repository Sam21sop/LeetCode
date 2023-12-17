class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid
        return left
    

if __name__ == '__main__':
    nums = [1,3,5,6]
    target = 5
    obj = Solution()
    res = obj.searchInsert(nums, target)
    print(res)