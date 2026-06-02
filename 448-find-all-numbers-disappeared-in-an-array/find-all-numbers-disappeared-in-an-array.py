class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        new_list=set(nums)
        l=[]
        for i in range(1,len(nums)+1):
            if i not in new_list:
                l.append(i)
        return l
        