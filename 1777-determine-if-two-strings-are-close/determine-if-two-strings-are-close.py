class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        l1=[]
        l2=[]
        for i in range(97,123):
            if chr(i) in word1 and chr(i) in word2:
                l1.append(word1.count(chr(i)))
                l2.append(word2.count(chr(i)))
            elif (chr(i) in word1 and chr(i) not in word2) or (chr(i) not in word1 and chr(i) in word2):
                return False
        return sorted(l1)==sorted(l2)

        