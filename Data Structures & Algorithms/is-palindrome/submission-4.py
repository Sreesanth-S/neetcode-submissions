class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = ""
        for i in s:
            if i.isalnum():
                tmp += i.lower()
        return tmp == tmp[::-1]