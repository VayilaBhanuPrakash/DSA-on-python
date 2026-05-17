class Solution:
    def countAndSay(self, n: int) -> str:
        def frequency(num):
            num=str(num)
            count=1
            res=""
            for i in range(1,len(num)):
                if num[i]==num[i-1]:
                    count+=1
                else:
                    res+=str(count)
                    res+=num[i-1]
                    count=1
            res+=str(count)
            res+=num[-1]
            return res
        res="1"
        for i in range(n-1):
            res=frequency(res)
            print(res)
        return res
        