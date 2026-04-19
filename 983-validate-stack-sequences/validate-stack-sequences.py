class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i=0
        j=0
        n=len(pushed)
        l=[]
        while i<n and j<n:
            flag=0
            while i<n: #and pushed[i]!=popped[j]:
                l.append(pushed[i])
                flag=1
                while j<n and l and popped[j]==l[-1]:
                    l.pop()
                    j+=1
                    flag=1
                i+=1
            if flag==0:
                return False
            """while j<n and popped[j]==l[-1]:
                l.pop()
                j+=1"""
        return len(l)==0

            


        