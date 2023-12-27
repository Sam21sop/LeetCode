class Solution:
    def isPalindrome(self, s:str) -> bool:
        # convert to lowercase and remove alphanumeric
        clean_string = ''.join(char.lower() for char in s if char.isalnum())

        # check if clean_string is palindrome 
        return clean_string == clean_string[::-1]
    

if __name__ == '__main__':
    # s = "A man, a plan, a canal: Panama"
    s = "race a car"
    obj = Solution()
    res = obj.isPalindrome(s)
    print(res)