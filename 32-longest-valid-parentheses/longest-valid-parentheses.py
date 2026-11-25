class Solution:
    def longestValidParentheses(self, s: str) -> int:
        open = 0
        close = 0
        max_len = 0
        for i in range(len(s)): 
            if s[i] == "(":
                open += 1
            else:
                close += 1
            
            if open == close:
                max_len = max(max_len, open + close)
            elif close > open:
                open = 0
                close = 0
        open = 0
        close = 0
        for i in range(len(s) -1, -1, -1):
            if s[i] == "(":
                close += 1
            else:
                open += 1
            
            if open == close:
                max_len = max(max_len, open + close)
            elif close > open:
                open = 0
                close = 0
        
        return max_len


        