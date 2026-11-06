class NumArray:

    def __init__(self, nums: list[int]):
        self.num = nums
        self.prefix = [0]
        summ = 0
        for ele in nums:
            summ = summ + ele
            self.prefix.append(summ)

        

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)