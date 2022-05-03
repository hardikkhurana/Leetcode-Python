class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr.sort(key=abs)
        dic=Counter(arr)
        for i in range(len(arr)):
            if dic[arr[i]]==0:
                continue
            if dic[arr[i]*2]==0:
                return False
            dic[arr[i]]-=1
            dic[arr[i]*2]-=1
        return True
                
        
        