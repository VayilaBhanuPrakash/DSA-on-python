class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor = 0
        z_flag = True
        for ele in nums:
            xor = xor ^ ele
            if ele != 0:
                z_flag = False
        if xor != 0:
            return len(nums)
        if xor == 0 and z_flag == True:
            return 0
        elif xor == 0 and z_flag == False:
            return len(nums) - 1
    
            






        
        
        