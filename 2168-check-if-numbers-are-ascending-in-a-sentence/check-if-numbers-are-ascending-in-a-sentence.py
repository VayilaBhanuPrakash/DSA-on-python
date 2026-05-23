class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums="0123456789"
        l=s.split(" ")
        flag=0
        for ele in l:
            if ele[0] in nums:
                if flag==0:
                    first=int(ele)
                    flag=1
                else:
                    if first>=int(ele):
                        return False
                    else:
                        first=int(ele)
            
        return True
        