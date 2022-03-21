class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d={}
        for i in range(len(s)):
            d[s[i]]=i
        size=0
        end_ind=0
        res=[]
        for i,c in enumerate(s):
            size+=1
            end_ind=max(end_ind,d[c])
            if i == end_ind:
                res.append(size)
                size=0
        return res
      