class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        h= [0,31,28,31,30,31,30,31,31,30,31,30,31]

        start = max(arriveAlice,arriveBob)
        end = min(leaveAlice,leaveBob)

        start_month = int(start[:2])
        end_month = int(end[:2])
        start_date = int(start[3:])
        end_date = int(end[3:])
        
        res = 0
        for i in range(start_month,end_month):
            res += h[i]
        if start_month < end_month or (start_month == end_month and start_date <= end_date):
            res = res + (end_date - start_date + 1)

        return res
        