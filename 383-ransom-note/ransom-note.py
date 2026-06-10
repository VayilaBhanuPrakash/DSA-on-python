class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        h1 = {}
        h2 = {}
        for ele in ransomNote:
            if ele in h1:
                h1[ele] += 1
            else:
                h1[ele] = 1
        for ele in magazine:
            if ele in h2:
                h2[ele] += 1
            else:
                h2[ele] = 1
        for keys in h1:
            if keys not in h2 or h1[keys] > h2[keys]:
                return False
        return True
        