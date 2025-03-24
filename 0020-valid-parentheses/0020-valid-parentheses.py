class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        if (len(s) % 2) != 0:
            return False  

        for char in s:
            if char in pairs.values():
                stack.append(char)
            elif char in pairs:
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
            else:
                return False

        if stack:
            return False
        else:
            return True