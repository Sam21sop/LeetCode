class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        list_to_tuple = tuple(nums)
        for i in range(len(list_to_tuple) - 1):
            for j in range(i+1, len(list_to_tuple)):
                if list_to_tuple[j] == target - list_to_tuple[i]:
                    return (i, j)
                

if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    obj = Solution()
    res = obj.twoSum(nums, target)
    print(res)