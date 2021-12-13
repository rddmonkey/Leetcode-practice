class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        count = 0
        
        for word in words:
            for i in range(len(word)):
                if word[i] in allowed and i == len(word) - 1:
                    count += 1
                if word[i] in allowed:
                    continue
                else: 
                    break
        
        return count
