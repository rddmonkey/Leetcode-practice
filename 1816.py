class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        
        slist = s.split()
        
        return " ".join(slist[:k])
