class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        h = {} 
        i = 0
        c = 0
        while c< len(nums):
            ele = nums[i]
            if ele in h:
                h[ele] += 1
            else:
                h[ele] = 1
            if h[ele] <= 2:
                count += 1
                i+=1
            else:
                nums.remove(ele)
                nums.append(0)
            c += 1
        return count

            

        