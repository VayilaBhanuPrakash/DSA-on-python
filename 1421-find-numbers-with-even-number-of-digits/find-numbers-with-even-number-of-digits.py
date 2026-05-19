class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for ele in nums:
            c=0
            while ele>0:
                ele=ele//10
                c+=1
            if c%2==0:
                count+=1
        return count

        