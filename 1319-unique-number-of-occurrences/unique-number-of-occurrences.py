class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        h={}
        for ele in arr:
            if ele in h:
                h[ele]+=1
            else:
                h[ele]=1
        s=set()
        for values in h.values():
            if values in s:
                return False
            else:
                s.add(values)
        return True
        
        