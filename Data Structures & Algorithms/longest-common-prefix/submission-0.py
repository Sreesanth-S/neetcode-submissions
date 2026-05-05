class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sub = strs[0]
        for i in strs[1:]:
            while not i.startswith(sub):
                sub = sub[:-1]
                if sub == "":
                    return ""
        return sub