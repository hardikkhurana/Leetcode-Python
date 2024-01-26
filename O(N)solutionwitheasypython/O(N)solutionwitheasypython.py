class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = deque(encoding)

    def next(self, n: int) -> int:
        while self.encoding:

            count, num = self.encoding.popleft(), self.encoding.popleft()
            if count >= n:
                self.encoding.appendleft(num)
                self.encoding.appendleft(count-n)
                return num
            n -= count
        return -1


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
