class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = set("abcdefghijklmnopqrstuvwxyz")

        for char in sentence:
            if char in alphabet:
                alphabet.remove(char)
        
        return len(alphabet) == 0
