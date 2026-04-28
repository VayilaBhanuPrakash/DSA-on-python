class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count=0
        dictt={}
        for ele1 in nums1:
            for ele2 in nums2:
                s1=ele1+ele2
                dictt[s1]=dictt.get(s1,0)+1
        for ele3 in nums3:
            for ele4 in nums4:
                s2=-(ele3+ele4)
                if s2 in dictt:
                    count+=dictt[s2]
        return count
            
                

        