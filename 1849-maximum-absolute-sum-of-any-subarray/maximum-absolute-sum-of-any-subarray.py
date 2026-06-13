class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        positive_sum = float('-inf')
        positive_maxsum = float('-inf')
        for ele in nums:
            positive_sum = max(positive_sum + ele , ele)
            positive_maxsum = max(positive_sum,positive_maxsum)
                

        negative_sum = float('inf')
        negetive_maxsum = float('inf')
        for ele in nums:
            negative_sum = min(negative_sum + ele , ele)
            negetive_maxsum = min(negative_sum,negetive_maxsum)

        
        return max(positive_maxsum,-negetive_maxsum)

        