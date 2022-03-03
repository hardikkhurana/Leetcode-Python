class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        a=tops[0]
        b=bottoms[0]
        ba=True
        bb=True
        for i in range(1,len(tops)):
            if a!=tops[i] and a!=bottoms[i]:
                ba=False
                break
        for i in range(1,len(tops)):
            if b!=tops[i] and b!=bottoms[i]:
                bb=False
                break
        if ba==False and bb==False:
            return -1
        u=l=0
        if ba:
            for i in range(len(tops)):
                if a!=tops[i]:
                    u+=1
                if a!=bottoms[i]:
                    l+=1
            return min(u,l)
        if bb:
            for i in range(len(tops)):
                if b!=tops[i]:
                    u+=1
                if b!=bottoms[i]:
                    l+=1
            return min(u,l)
        