class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s=set()
        for ele in sentence:
            s.add(ele)
        return len(s)==26
        