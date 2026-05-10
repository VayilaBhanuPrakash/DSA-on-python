class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        stack=[]
        index=[]
        res=[0 for i in range(n)]
        for i in range(n-1,-1,-1):
            while stack and stack[-1]<=temperatures[i]:
                stack.pop()
                index.pop()
            if stack:
                res[i]=index[-1]-i
            stack.append(temperatures[i])
            index.append(i)
        return res
        