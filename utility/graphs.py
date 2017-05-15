from typing import Dict, List, Tuple


class Vertex:
    def __init__(self, _adj: Dict[int, int] = None):
        self.adj = _adj

    @classmethod
    def with_adj_vertices(cls, adj: Dict[int, int]):
        return cls(adj)


class Graph:
    def __init__(self):
        self.V = {}         # type: Dict[int, Vertex]
        self.E = []         # type: List[Tuple[int, Tuple[int, int]]]
