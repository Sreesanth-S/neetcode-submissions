class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub={}
        j = 0
        max_len=0
        for i in range(len(s)):
            if s[i] in sub:
                j = max(sub[s[i]]+1, j)
            sub[s[i]] = i
            max_len = max(max_len, i-j+1)
        return max_len
