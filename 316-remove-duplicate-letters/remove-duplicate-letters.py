class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_index = [-1] * 26
        for i in range(len(s)):
            last_index[ord(s[i]) - ord("a")] = i
        
        stack = []
        visited = [False] * 26
        for i in range(len(s)):
            if visited[ord(s[i]) - ord("a")] == True:
                continue
            
            while stack and stack[-1] > s[i] and last_index[ord(stack[-1]) - ord("a")] > i:
                visited[ord(stack[-1]) - ord("a")] = False
                stack.pop()

            stack.append(s[i])
            visited[ord(s[i]) - ord("a")] = True
        
        return "".join(stack)

        