class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1,0])
        restrictions.append([n,n-1])
        restrictions.sort()
        n = len(restrictions)

        for i in range(1,n):
            b1,h1 = restrictions[i-1]
            b2,h2 = restrictions[i]
            difference = b2 - b1
            restrictions[i][1] = min(h2,h1+difference)

        for i in range(n-2,0,-1):
            b1,h1 = restrictions[i]
            b2,h2 = restrictions[i+1]
            difference = b2 - b1
            restrictions[i][1] = min(h1,h2+difference)

        res = 0
        for i in range(1,n):
            b1,h1 = restrictions[i-1]
            b2,h2 = restrictions[i]
            difference = b2 - b1
            peak = (h1 + h2 + difference)//2
            res = max(res,peak)
        return res

        



        