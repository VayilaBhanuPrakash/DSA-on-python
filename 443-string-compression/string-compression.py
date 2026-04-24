class Solution:
    def compress(self, chars: List[str]) -> int:
        index=0
        i=0
        while i<len(chars):
            char=chars[i]
            count=0
            while i<len(chars) and chars[i]==char:
                i+=1
                count+=1
            chars[index]=char
            index+=1
            if count>1:
                for ele in str(count):
                    chars[index]=ele
                    index+=1
        return index
                






























        """n=len(chars)
        if n==1:
            return 1
        l=[ele for ele in chars]
        first=chars[0]
        count=1
        index=1
        for i in range(1,n):
            if first==l[i]:
                count+=1
            else:
                if count>1:
                    if index==1:
                        pass
                    else:
                        chars[index]=first
                        index+=1
                    s=str(count)
                    for ele in s:
                        chars[index]=ele
                        index+=1
                else:
                    chars[index]=l[i]
                    index+=1
                count=1
                first=l[i]
        if first!=chars[0] or index>1:
            chars[index]=first
            index+=1
        if count>1:
            s=str(count)
            for ele in s:
                chars[index]=ele
                index+=1
        return index"""

        