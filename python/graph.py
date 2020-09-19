class Node:
    def __init__(self):
        self.status = 0


class Graph:
    def __init__(self, n, edges, directed=False):
        self.nodes = []
        self.directed = directed
        self.n = n
        for i in range(self.n + 1):
            self.nodes.append(Node())
        self.e = [[] for _ in range(self.n + 1)]
        for ed in edges:
            self.e[ed[0]].append(ed[1])
            if not directed:
                self.e[ed[1]].append(ed[0])

    def dfs(self, k, past):
        self.nodes[k].status = 1
        for y in self.e[k]:
            if y == past and not self.directed:
                continue
            if self.nodes[y].status == 0:
                self.dfs(y, k)
                if self.loopFound == 1:
                    if k == self.loop[0]:
                        self.loopFound = 2
                    else:
                        self.loop.append(k)
                if self.loopFound:
                    return
            elif self.nodes[y].status == 1:
                self.loopFound = 1
                self.loop.append(y)
                self.loop.append(k)
                return
        self.nodes[k].status = 2

    def findLoop(self):
        self.loopFound = 0
        self.loop = []
        self.dfs(1, -1)


if __name__ == '__main__':
    g = Graph(2, [[1, 2], [2, 1]], directed=True)
    g.findLoop()
    print(g.loop)