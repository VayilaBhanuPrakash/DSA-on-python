class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse=True)
        tasks.sort()
        min_time=0
        for i in range(len(tasks)):
            min_time=max(min_time,tasks[i]+processorTime[i//4])
        return min_time


        