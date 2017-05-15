class DisjointSet:
    def __init__(self):
        self.parents = dict()   # type: dict
        self.ranks = dict()     # type: dict

    def make_set(self, i):
        self.parents[i] = i
        self.ranks[i] = 0

    def find(self, i):
        if i != self.parents[i]:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    def union(self, i, j):
        _i = self.find(i)
        _j = self.find(j)

        if _i == j:
            return

        if self.ranks[_i] > self.ranks[_j]:
            self.parents[_j] = _i
        else:
            self.parents[_i] = _j
            if self.ranks[_i] == self.ranks[_j]:
                self.ranks[_j] += 1