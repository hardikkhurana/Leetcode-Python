import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res=""
        h=[]
        for i in ([(-a,"a"),(-b,"b"),(-c,"c")]):
            count,char=i
            if count!=0:
                heapq.heappush(h,(count,char))
        while h:
            count1,char1=heapq.heappop(h)
            if len(res)>1 and res[-1]==res[-2]==char1:
                if not h:
                    break
                count2,char2=heapq.heappop(h)
                res+=char2
                count2+=1
                if count2:
                    heapq.heappush(h,(count2,char2))
            else:
                res+=char1
                count1+=1
            if count1:
                heapq.heappush(h,(count1,char1))
        return res
            