class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ab = bin(a)[2:]
        bb = bin(b)[2:]
        cb = bin(c)[2:]
        n1=len(ab)
        n2=len(bb)
        n3=len(cb)
        count=0
        for i in range(-1,-n3-1,-1):
            abi = int(ab[i]) if i >= -n1 else 0
            bbi = int(bb[i]) if i >= -n2 else 0
            cbi=int(cb[i])
            if cbi == 0:
                if abi | bbi== 0:
                    pass
                elif abi == 1 and bbi == 1:
                    count += 2
                else:
                    count += 1
            else:
                if abi | bbi == 1:
                    pass
                else:
                    count+=1
        index = -n3-1
        while index > -n1-1:
            if ab[index] == "1":
                count += 1
            index -= 1
        index1 =- n3-1
        while index1 >- n2-1:
            if bb[index1] == "1":
                count += 1
            index1 -= 1
        return count
        