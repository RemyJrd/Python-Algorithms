class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}

        for word in strs:
            signature = ''.join(sorted(word))

            if signature not in grouped:
                grouped[signature] = []
        
            grouped[signature].append(word)
        
        return list(grouped.values())
        