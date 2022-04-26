class UndergroundSystem:
    def __init__(self):
        self.checkins = defaultdict()
        self.routes = defaultdict()
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = (stationName, t)
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        stn, start = self.checkins[id]
        del self.checkins[id]
        route = stn + "," + stationName
        if route not in self.routes: self.routes[route] = [0,0]
        trip = self.routes[route]
        trip[0] += 1
        trip[1] += t - start
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        count, rsum = self.routes[startStation + "," + endStation]
        return rsum / count