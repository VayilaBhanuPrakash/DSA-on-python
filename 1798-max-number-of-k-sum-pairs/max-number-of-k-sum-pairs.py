class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count=0
        dictt={}
        for ele in nums:
            dictt[ele]=dictt.get(ele,0)+1
        for key in dictt:
            if k-key in dictt and key<=k-key:
                if key!=k-key:
                    count+=min(dictt[key],dictt[k-key])
                else:
                    count+=dictt[key]//2 
        return count



                    



        