class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        mp={}
        for i in words2:
            temp=Counter(i)
            for j in temp:
                if j in mp:
                    mp[j]=max(temp[j],mp[j])
                else:
                    mp[j]=temp[j]
        res=[]
        for i in words1:
            check=Counter(i)
            ans=True
            for p in mp:
                q=mp[p]
                if p in check:
                    if check[p]<q:
                        ans=False
                        break                   
                else:
                    ans=False
                    break
            if ans==True:
                res.append(i)
        return res