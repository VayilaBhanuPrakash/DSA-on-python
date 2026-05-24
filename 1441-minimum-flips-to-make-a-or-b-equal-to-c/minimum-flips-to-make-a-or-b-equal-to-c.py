class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ab = bin(a)[2:]
        bb = bin(b)[2:]
        cb = bin(c)[2:]
        count=0
        for i in range(-1,-len(cb)-1,-1):
            abi = int(ab[i]) if i >= -len(ab) else 0
            bbi = int(bb[i]) if i >= -len(bb) else 0
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
        index=-len(cb)-1
        while index>-len(ab)-1:
            if ab[index]=="1":
                count+=1
            index -= 1
        index1 =- len(cb)-1
        while index1 >- len(bb)-1:
            if bb[index1] == "1":
                count += 1
            index1 -= 1
        return count
            


