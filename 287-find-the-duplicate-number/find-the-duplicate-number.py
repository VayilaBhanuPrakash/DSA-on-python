class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = set()
        for ele in nums:
            if ele in s:
                return ele
            s.add(ele)
            
        
        