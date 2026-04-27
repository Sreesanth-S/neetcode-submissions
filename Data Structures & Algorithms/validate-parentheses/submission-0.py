class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")":"(", "}":"{", "]":"["}
        for i in s:
            if i in brackets:
                top = stack.pop() if stack else "#"
                if top != brackets[i]:
                    return False
            else:
                stack.append(i)
        if stack:
            return False
        return True