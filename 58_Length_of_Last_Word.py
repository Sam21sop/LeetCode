class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
    


if __name__ == '__main__':
    s = "   fly me   to   the moon  "
    # print(s.split())
    obj = Solution()
    res = obj.lengthOfLastWord(s)
    print(res)