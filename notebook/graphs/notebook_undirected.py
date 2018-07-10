from utils import to_graphviz

class Clock:
    def __init__(self):
        self._current = 0
    
    def current(self):
        return self._current

    def next(self):
        self._current += 1


def dfs(graph: dict):
    visited = dict()
    cc = dict()
    _c = 1
    prev = dict()
    post = dict()
    clock = Clock()

    for e in graph.keys():
        if e not in visited:
            explore(graph, e, _c, visited, cc, prev, post, clock)
            _c += 1
    return visited, cc, prev, post


def explore(graph: dict, v: str, _c: int, visited: dict, cc: dict, prev: dict, post: dict, clock: Clock):
    pre_visit(v, prev, clock)
    visited[v] = True
    cc[v] = _c
    for e in graph[v]:
        if e not in visited:
            explore(graph, e, _c, visited, cc, prev, post, clock)
    post_visit(v, post, clock)


def pre_visit(v: str, prev: dict, clock: Clock):
    prev[v] = clock.current()
    clock.next()


def post_visit(v: str, post: dict, clock: Clock):
    post[v] = clock.current()
    clock.next()


def bfs(graph: dict):
    pass


g = {
    'A': ['B', 'C', 'D'],
    'B': ['A'],
    'C': ['A', 'D'],
    'D': ['A', 'C'],
    'E': ['F'],
    'F': ['E'],
    'G': ['H', 'I'],
    'H': ['G', 'I'],
    'I': ['G', 'H']
}


v, c, prev, post = dfs(g)
print(v)
print(c)
print(prev)
print(post)
print(to_graphviz(g, c, prev, post, dir='dir'))