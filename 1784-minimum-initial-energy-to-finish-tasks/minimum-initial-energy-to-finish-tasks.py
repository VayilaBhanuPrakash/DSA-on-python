class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x:x[1]-x[0],reverse=True)
        print(tasks)
        sum=tasks[0][1]
        rem=tasks[0][1]-tasks[0][0]
        for i in range(1,len(tasks)):
            if rem<tasks[i][1]:
                print(rem,tasks[i][1])
                add=tasks[i][1]-rem
                rem+=add
                sum+=add
                print(sum)
            rem=rem-tasks[i][0]
        return sum
            


        """minn=tasks[0][1]-tasks[0][0]
        maxx=tasks[0][1]
        sum=0
        for ele in tasks:
            sum+=ele[0]
            minn=min(minn,ele[1]-ele[0])
            maxx=max(maxx,ele[1])
        if sum+minn<=maxx:
            return maxx
        return sum+minn"""
        
        