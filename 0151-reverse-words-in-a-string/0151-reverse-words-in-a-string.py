class Solution:
    def reverseWords(self, s: str) -> str:
        string_builder = collections.deque()

        start = -1
        i = 0
        while i < len(s):
           if  s[i] != " ":
            start = i
            while i < len(s) and s[i] != " ":
                i += 1
            string_builder.appendleft(s[start: i])
            i -= 1
           i += 1
        return " ".join(string_builder) 

        