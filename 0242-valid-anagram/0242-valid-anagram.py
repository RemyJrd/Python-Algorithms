class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        
        for strings in s:
            seen[strings] = seen.get(strings, 0) + 1
        
        for stringt in t:
            if stringt not in seen or seen[stringt] == 0:
                return False
            seen[stringt] -= 1
        
        for val in seen.values():
            if val != 0:
                return False
        
        return True