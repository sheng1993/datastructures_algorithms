
"""Tries of Patterns
Create tree with every pattern
O(n) = O(|Text| * |LongestPattern|)
O(n) = |Text| * |Patterns|
"""

"""Suffix Trie of Text
Create Tree from text with all suffix
Memory O(n) = |Text| * (|Text| - 1)/2
"""

"""Suffix Tree
Combining the edges of any non-branching path into a single edge.
Fast O(|Text|) algorithm for building the SuffixTree(Text)
O(|Text| + |Patterns|)
Memory O(|Text|)
"""