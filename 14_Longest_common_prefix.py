class Solution:
    def _commonString(self, s1:str, s2:str) -> str:
        min_len_word = min(len(s1), len(s2))
        common_prefix = ''
        for i in range(min_len_word):
            if s1[i] == s2[i]:
                common_prefix = common_prefix + s1[i]
            else:
                break
        return common_prefix
    

    def longestCommonPrefix(self, strs:list[str]) -> str:
        if '' in strs or strs == []:
            return ''
        result = strs[0]
        for i in range(1, len(strs)):
            result = self._commonString(result, strs[i])
        return result
    

if __name__ == '__main__':
    obj = Solution()
    str_lst = ['flower', 'flow', 'fly']
    result = obj.longestCommonPrefix(str_lst)
    print(result)