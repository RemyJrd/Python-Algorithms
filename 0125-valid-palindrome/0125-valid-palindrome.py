class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanstring = ''
        left = 0

        for char in s:
            if char.isalnum():
                cleanstring += char.lower()
        
        right = len(cleanstring) - 1
        while left < right:
            if cleanstring[left] != cleanstring[right]:
                return False
                
            left +=1
            right -= 1

        
        return True
        