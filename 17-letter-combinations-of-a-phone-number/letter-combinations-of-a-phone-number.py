class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapp={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        l=[]
        n=len(digits)
        for ele in mapp[int(digits[0])]:
            if n==1:
                l.append(ele)
            else:
                s=ele
                for ele1 in mapp[int(digits[1])]:
                    if n==2:
                        l.append(s+ele1)
                    else:
                        s=ele+ele1
                        for ele2 in mapp[int(digits[2])]:
                            if n==3:
                                l.append(s+ele2)
                            else:
                                s=ele+ele1+ele2
                                for ele3 in mapp[int(digits[3])]:
                                    l.append(s+ele3)

        return l
                
        