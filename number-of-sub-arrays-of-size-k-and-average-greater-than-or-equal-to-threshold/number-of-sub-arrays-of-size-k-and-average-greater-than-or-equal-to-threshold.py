class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        s=0
        res=0
        for i in range(k):
            s+=arr[i]
        if s/k>=threshold:
            res+=1
        i=0
        j=k
        while j<len(arr):
            s-=arr[i]
            s+=arr[j]
            if s/k>=threshold:
                res+=1
            i+=1
            j+=1
        return res
        