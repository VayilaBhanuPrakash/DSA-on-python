class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        res = []
        for ele in bulbs:
            if ele not in res:
                res.append(ele)
            else:
                res.remove(ele)
        return sorted(res)
        