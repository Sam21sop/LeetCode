class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        index = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index
    
    # def removeElement(self, nums: list[int], val: int) -> int:
    #     if not nums:
    #         return 0
    #     i = 0
    #     k = 0
    #     while i < len(nums):
    #         if nums[i] != val:
    #             nums[k] = nums[i]
    #             k += 1
    #         i += 1
    #     return k
    


if __name__ == "__main__":
    array = [3, 2, 2, 3]
    val = 3
    obj = Solution()
    res = obj.removeElement(array, val)
    print(res)