def to_graphviz(g: dict, cc: dict, prev: dict, post: dict, dir='none', copy=True):
    if dir == 'none':
        from graphviz import Graph as graph
    elif dir == 'dir':
        from graphviz import Digraph as graph
    else:
        raise Exception('Not valid dir value.')

    dot = graph()
    
    for v in g.keys():
        dot.node(v, label=v + ': ' + str(prev[v]) + '/' + str(post[v]))
        for e in g[v]:
            dot.edge(v, e)

    if copy:
        import pyperclip
        pyperclip.copy(dot.source)
        print('Graphviz source copied to clipboard.')

    return dot.source


class disjointset:
    def __init__(self, *args, **kwargs):
        self.parents = dict()
        self.ranks = dict()

    def __contains__(self, v):
        return v in self.parents
    
    def add(self, value):
        self.parents[value] = value
        self.ranks[value] = 1
    
    def find(self, value):
        if value != self.parents[value]:
            self.parents[value] = self.find(self.parents[value])
        return self.parents[value]
    
    def union(self, value1, value2):
        _v1 = self.find(value1)
        _v2 = self.find(value2)

        if _v1 == _v2:
            return
        
        if self.ranks[_v1] > self.ranks[_v2]:
            self.parents[_v2] = _v1
        else:
            self.parents[_v1] = _v2
            if self.ranks[_v1] == self.ranks[_v2]:
                self.ranks[_v2] += 1
