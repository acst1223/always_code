class FindSet(object):
    def __init__(self, n):
        self.l = [i for i in range(n)]

    def findRoot(self, x):
        if self.l[x] == x:
            return x, 0
        self.l[x], d = self.findRoot(self.l[x])
        return self.l[x], d + 1

    def merge(self, a, b):
        a, da = self.findRoot(a)
        b, db = self.findRoot(b)
        if a != b:
            if da > db:
                self.l[b] = a
            else:
                self.l[a] = b

    def query(self, a, b):
        a, _ = self.findRoot(a)
        b, _ = self.findRoot(b)
        return a == b