class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)
        res = []
        for ele in spells:
            left = 0
            right = n-1
            while left <= right:
                mid = left + (right - left) // 2
                if mid+1<n and potions[mid]*ele < success and potions[mid+1]*ele >= success:
                    res.append(n-mid-1)
                    break
                elif mid==0 and potions[mid]*ele >= success:
                    res.append(n)
                    break
                elif potions[mid]*ele < success:
                    left =mid + 1
                else:
                    right =mid - 1

            else:
                res.append(0)
        return res
        