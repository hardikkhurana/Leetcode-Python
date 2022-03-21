class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[-1]*len(nums1)
        d=dict()
        
        for e,f in enumerate(nums2):
            d[f]=e
        for i in range(len(nums1)):
            ele=nums1[i]
            m=d[ele]
            for j in range(int(m),len(nums2)):
                if nums2[j]>ele:
                    res[i]=nums2[j]
                    break
        return res
                    
                
            
                
        