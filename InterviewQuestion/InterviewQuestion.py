# heap nlogn
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda x:x[1])

        h = []
        time = 0

        for t,l in courses:
            if t+ time <=l:
                time+=t
                heappush(h,-t)
            elif h and -h[0]>t:
                time += heappop(h)
                time += t
                heappush(h,-t)

        return len(h) 
# dp n^2 #TLE
class Solution1:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda x:x[1])

        memo = {}

        def helper(ind,time):
            if (ind,time) in memo:
                return memo[(ind,time)]

        
