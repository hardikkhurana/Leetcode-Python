        self.tree = [0]*(2*n)
        self.n = n
        for i in range(n):
            self.tree[i+n] = nums[i]
        for i in range(n-1, -1, -1):
            self.tree[i] = self.tree[2*i]+self.tree[2*i+1]

    def update(self, index: int, val: int) -> None:
        index = index+self.n
        self.tree[index] = val
        i = index//2
        while i>=1:
            self.tree[i] = self.tree[2*i]+self.tree[2*i+1]
            i = i//2

    def sumRange(self, left: int, right: int) -> int:
        left = left+self.n
        right = right+self.n
        s = 0
        while left<=right:
            if left%2==1:
                s = s+self.tree[left]
                left+=1
            if right%2==0:
                s = s+self.tree[right]
                right-=1

    def __init__(self, nums: List[int]):
        n = len(nums)
class NumArray:
