class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        shash = 0
        thash = 0
        i = len(s) - 1
        j = len(t) - 1

        while i >= 0 or j >= 0:
            while i >= 0:
                if s[i] == "#":
                    shash += 1
                    i -= 1
                elif shash > 0:
                    shash -= 1
                    i -= 1
                else:
                    break
            while j >= 0:
                if t[j] == "#":
                    thash += 1
                    j -= 1
                elif thash > 0:
                    thash -= 1
                    j -= 1
                else:
                    break
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            else:
                if i >=0 or j >= 0:
                    return False
            
            i -= 1
            j -= 1
        return True


        
        