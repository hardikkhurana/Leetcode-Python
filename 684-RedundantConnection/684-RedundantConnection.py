#https://leetcode.com/problems/minimum-number-of-refueling-stops/solutions/2455515/
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> 
int:
        stations.append([target, 0])
        if startFuel >= target:
            return 0
        stops = 0 
        reach = startFuel
        heap = []

        for pos, fuel in stations:
            while reach<pos:
                if not heap:
                    return -1
                reach += (-1* heappop(heap))
                stops+=1
                if reach>=target:
                    return stops
            heappush(heap,-fuel)


class Solution:
plan-your-road-trip-in-advance-clear-explanation-o-nlogn-python-heap/
