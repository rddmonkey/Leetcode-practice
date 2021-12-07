class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        import string

        alphabet_string = string.ascii_lowercase

        abcs = list(alphabet_string)
        
        letters = [x for x in sentence]
        
        return set(abcs) == set(letters)
