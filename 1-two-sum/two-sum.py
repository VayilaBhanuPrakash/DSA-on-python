class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        i=0
        for ele in nums:
            if target-ele in h:
                first=h[target-ele]
                second=i
                return first,second
            else:
                h[ele]=i
            i+=1
        