class Solution:
    def rotatedDigits(self, n: int) -> int:
        """count=0
        if n<=10:
            sett={2,5,6,9}
            for i in range(1,n+1):
                if i in sett:
                    count+=1
            return count
        count=4
        sett1={2,5,6,9}
        sett2={0,1,8}
        for i in range(12,n+1):
            flag1=0
            flag2=0
            c=0
            while i>0:
                rem=i%10
                i=i//10
                c+=1
                if rem in sett1:
                    flag1+=1
                elif rem in sett2:
                    flag2+=1
            if c==flag1+flag2 and flag1:
                count+=1
        return count"""
        count=0
        for i in range(1,n+1):
            s=str(i)
            if "3" in s or "4" in s or "7" in s:
                continue
            elif "2" in s or"5" in s or "6" in s or "9" in s:
                count+=1
        return count
        