import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i,task in enumerate(tasks):
            task.append(i)
        tasks.sort()
        time=tasks[0][0]
        minheap=[]
        i=0
        res=[]
        while i<len(tasks) or minheap:
            while i<len(tasks) and time>=tasks[i][0]:
                heapq.heappush(minheap,(tasks[i][1],tasks[i][2]))
                i+=1
            if len(minheap)==0:
                time=tasks[i][0]
                continue
            timeTaken,index=heapq.heappop(minheap)
            res.append(index)
            time+=timeTaken
        return res