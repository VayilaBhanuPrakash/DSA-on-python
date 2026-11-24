class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process(st):
            stack = []
            for ele in st:
                if ele == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(ele)
            return stack
        
        return process(s) == process(t)

        
        