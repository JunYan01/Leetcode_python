1396Design Underground System

class UndergroundSystem:

    def __init__(self):
        self.checkInHash = {}
        self.getAverageTimeStation = {}
        # return

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInHash[id] = (stationName,t)
        # print(stationName,t)
        # return
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        inStantion, tStart = self.checkInHash[id]
        inOutStantion = inStantion + stationName
        a, b = self.getAverageTimeStation.get(inOutStantion,(0,0))
        self.getAverageTimeStation[inOutStantion] =  (a+t-tStart,b+1)
        # self.getAverageTimeStation[inOutStantion] =  (self.getAverageTimeStation.get(inOutStantion,(0,0))[0]+t-tStart,self.getAverageTimeStation.get(inOutStantion,(0,0))[1]+1)
        # print(self.getAverageTime[inOutStantion])
        # print(self.checkIn[id])
        del self.checkInHash[id] 
        # return
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        # print(self.getAverageTimeStation[startStation+endStation])
        a, b = self.getAverageTimeStation[startStation+endStation]
        # print(a,b)
        return a/b
        
# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)