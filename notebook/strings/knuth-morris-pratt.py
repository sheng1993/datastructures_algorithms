import sys

"""Definition
Border of string S is a prefix of S which is
equal to a suffix of S, but not equal to the whole S.
Example:
'a' is border of 'arba'
'ab' is a border of 'abcdab'
'abab' is a border of 'ababab'
'ab' is not a border of 'ab'
"""


"""
Building prefix = O(|p| + |t|)
Finding occurrences = O(|p| + |t|)
"""

def compute_prefix_function(p):
    s = [-1] * len(p)
    s[0] = 0
    border = 0
    for i in range(1, len(p)):
        while border > 0 and p[i] != p[border]:
            border = s[border - 1]
        if p[i] == p[border]:
            border += 1
        else:
            border = 0
        s[i] = border
    return s


def find_all_occurrences(p, t):
    S = p + '$' + t
    s = compute_prefix_function(S)
    result = list()
    len_p = len(p)
    for i in range(len_p + 1, len(s)):
        if s[i] == len_p:
            result.append(i - (2 * len_p))
    return result


print(compute_prefix_function('abababcaab'))
print(find_all_occurrences('aba', 'abababcaab'))