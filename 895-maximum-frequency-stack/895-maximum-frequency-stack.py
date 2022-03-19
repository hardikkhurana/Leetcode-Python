from collections import defaultdict,Counter
class FreqStack:
    def __init__(self):
        self.freq=Counter()
        self.d=defaultdict(list)
        self.maxf=0
        
    def push(self, val: int) -> None:
        self.freq[val] +=1
        self.maxf = max(self.maxf, self.freq[val])
        self.d[self.freq[val]].append(val)

    def pop(self) -> int:
        freq, m, maxf = self.freq, self.d, self.maxf
        x = m[maxf].pop()
        if not m[maxf]: self.maxf = maxf - 1
        freq[x] -= 1
        return x
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()