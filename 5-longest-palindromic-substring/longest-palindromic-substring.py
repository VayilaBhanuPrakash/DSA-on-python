class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        start = 0
        end = 0
        n = len(s)
        for i in range(n):

            first = i
            last = i
            while first >= 0 and last < n and s[first] == s[last]:
                if last - first > end - start:
                    start = first
                    end = last
                first -= 1
                last += 1

            first = i
            last = i + 1
            while first >= 0 and last < n and s[first] == s[last]:
                if last - first > end - start:
                    start = first
                    end = last
                first -= 1
                last += 1
        return s[start : end + 1]
        