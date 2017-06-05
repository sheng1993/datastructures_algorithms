# python3
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

NA = -1


class Node:
	def __init__ (self):
		self.next = [NA] * 4


def prefix_trie_matching(text, trie):
	i = 0
	symbol = text[0]
	v = 0
	while True:
		if v not in trie:
			return 1
		elif symbol in trie[v]:
			v = trie[v][symbol]
			i += 1
			if i < len(text):
				symbol = text[i]
			elif v in trie:
				return -1

		else:
			return -1


def solve (text, n, patterns):
	result = []
	trie = build_trie(patterns)
	i = 0
	while i < len(text):
		if prefix_trie_matching(text[i:], trie) > 0:
			result.append(i)
		i += 1
	return result

text = sys.stdin.readline().strip ()
n = int (sys.stdin.readline().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline().strip()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
