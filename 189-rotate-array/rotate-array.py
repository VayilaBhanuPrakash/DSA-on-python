class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        temp = [ele for ele in nums]
        for i in range(n):
            index = (i + k) % n
            nums[index] = temp[i]
            

        