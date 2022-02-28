class Solution:
    def findComplement(self, num: int) -> int:
        binary = list(bin(num))
        for i in range(2,len(binary)):
            if binary[i] == "1":
                binary[i] = "0"
            else:
                binary[i] = "1"
        res = ''.join(binary)
        return int(res,2)
        