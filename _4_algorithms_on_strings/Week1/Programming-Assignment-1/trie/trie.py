#Uses python3
import sys
from typing import List, Dict

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
def build_trie(patterns: List[str]):
    tree = dict()   # type: Dict[int, Dict[str, int]]
    # write your code here
    cont = 0
    node = 0
    for pattern in patterns:
        for x in pattern:
            if node not in tree:
                tree[node] = dict()
            if x in tree[node]:
                node = tree[node][x]
            else:
                cont += 1
                tree[node][x] = cont
                node = cont
        node = 0
    return tree


def build_trie_2(patterns: List[str]):
    tree = dict()  # type: Dict[int, Dict[str, int]]
    root = 0
    nodeCount = 0
    for pattern in patterns:
        currentNode = root
        for i in range(0, len(pattern)):
            if currentNode not in tree:
                tree[currentNode] = dict()
            currentSymbol = pattern[i]
            if currentSymbol in tree[currentNode]:
                currentNode = tree[currentNode][currentSymbol]
            else:
                nodeCount += 1
                tree[nodeCount] = dict()
                tree[currentNode][currentSymbol] = nodeCount
                currentNode = nodeCount
    return tree


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie_2(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
