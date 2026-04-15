class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """count=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if sum(nums[i:j+1])==k:
                    count+=1
        return count"""
        prefix_sum=0
        count=0
        hashmap={0:1}
        for num in nums:
            prefix_sum+=num
            if prefix_sum-k in hashmap:
                count+=hashmap[prefix_sum-k]
            if prefix_sum in hashmap:
                hashmap[prefix_sum]+=1
            else:
                hashmap[prefix_sum]=1
            #hashmap[prefix_sum]=hashmap.get(prefix_sum,0)+1
        return count
        
            

            
            
        
        