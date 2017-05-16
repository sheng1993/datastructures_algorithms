from typing import Dict, List, Tuple


class Vertex:
    def __init__(self, _adj: Dict[int, int]=None):
        if _adj is None:
            self.adj = {}
        else:
            self.adj = _adj

    @classmethod
    def with_adj_vertices(cls, adj: Dict[int, int]):
        return cls(adj)


class Graph:
    def __init__(self):
        self.V = {}         # type: Dict[int, Vertex]
        self.E = []         # type: List[Tuple[int, Tuple[int, int]]]


def reverse_graph(graph: Graph):
    gr = Graph()
    for v in graph.V.keys():
        if v not in gr.V:
            gr.V[v] = Vertex()
        for e in graph.V[v].adj.keys():
            if e not in gr.V:
                gr.V[e] = Vertex()
            gr.V[e].adj[v] = graph.V[v].adj[e]
    return gr
