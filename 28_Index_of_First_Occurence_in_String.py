class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
        

if __name__ == '__main__':
    haystack = "sadbutsad"
    needle = "sad"
    obj = Solution()
    res = obj.strStr(haystack, needle)
    print(res)