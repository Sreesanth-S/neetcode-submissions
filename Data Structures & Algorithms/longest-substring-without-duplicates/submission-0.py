class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub=""
        max_len=0
        for i in s:
            if i in sub:
                sub = sub[sub.index(i)+ 1:]
            sub += i
            if len(sub) > max_len:
                max_len = len(sub)
        return max_len
