def to_graphviz(g: dict, cc: dict, prev: dict, post: dict, dir='none'):
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

    return dot.source