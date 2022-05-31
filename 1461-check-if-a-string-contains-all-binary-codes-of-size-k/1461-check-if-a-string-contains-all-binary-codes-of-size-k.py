class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        different_codes=set()
        for i in range(len(s)-k+1):
            different_codes.add(s[i:i+k])
        return len(different_codes)==2**k