class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h = ((hour * 60 + minutes) / (12 * 60)) * 360
        m = (minutes / 60)*360
        res = abs(h % 360 - m % 360)
        return min(res,360 - res)
        