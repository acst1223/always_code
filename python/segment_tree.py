class SegmentNode:
    def __init__(self, lo, hi):
        self.lo = lo
        self.hi = hi
        self.val = 0
        self.mid = None
        self.left = None
        self.right = None

    def insert(self, lo, hi, val=1):
        if lo == self.lo and hi == self.hi:
            self.val += 1
            return
        if not self.mid:
            self.mid = (self.lo + self.hi) // 2
            self.left = SegmentNode(self.lo, self.mid)
            self.right = SegmentNode(self.mid, self.hi)
        if lo >= self.mid:
            self.right.insert(lo, hi, val)
            return
        if hi <= self.mid:
            self.left.insert(lo, hi, val)
            return
        self.left.insert(lo, self.mid, val)
        self.right.insert(self.mid, hi, val)

    def query(self, pos):
        if not self.mid:
            return self.val
        if pos < self.mid:
            return self.val + self.left.query(pos)
        else:
            return self.val + self.right.query(pos)


class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.root = SegmentNode(0, n)

    def insert(self, lo, hi):
        self.root.insert(lo, hi)

    def query(self, pos):
        return self.root.query(pos)