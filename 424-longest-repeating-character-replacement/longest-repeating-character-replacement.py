class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for ch in range(26):
            count = 0
            i = 0
            for j in range(len(s)):
                if s[j] != chr(ch + 65):
                    count += 1
                    if count > k:
                        res = max(res, j - i)
                        while count > k and i < len(s):
                            if s[i] != chr(ch + 65):
                                count -=1
                            i += 1
                            
            if count <= k:
                res = max(res, j - i + 1)
            
        return res

        