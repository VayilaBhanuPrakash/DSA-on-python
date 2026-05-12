class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x:x[1]-x[0],reverse=True)
        sum=tasks[0][1]
        rem=tasks[0][1]-tasks[0][0]
        for i in range(1,len(tasks)):
            if rem<tasks[i][1]:
                add=tasks[i][1]-rem
                sum+=add
                rem+=add
            rem=rem-tasks[i][0]
        return sum
        