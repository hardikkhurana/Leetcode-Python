class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x:x[1])
        heap=[]
        time=0
        
        for c in courses:
            if time+c[0]<=c[1]:
                time+=c[0]
                heapq.heappush(heap, -1 * (c[0]))
            
            elif len(heap)!=0 and heap[0]*-1>c[0]:
                time -= (- 1 * heapq.heappop(heap))
                time += c[0]
                heapq.heappush(heap, -1 * (c[0]))
                
        return len(heap)
                