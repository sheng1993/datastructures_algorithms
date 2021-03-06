import math

'''
Answer #1- What do you think being a data scientist means?
    Some who uses data to extract information that can be used to improve
    a lot of thing that we do in daily basis.
    I would like to become one because many things we use in our life(technologies)
    uses machine learning and it is a field I really like and enjoy, and it would be
    exciting to work in it.


Answer #2 something amazing you have done outside a computer:   N/A



Answer #3 friendship paradox:   N/A - *Investigated: Most people have less friends than their own friends
                                        because people with more friends are more likely to be counted as
                                        one of your friends.



Answer #4:
    The expected percentage would be ~50% for girls and boys
'''


'''SECOND ROUND'''

'''
Answer #5
Binary search with validation for rotation check.
'''


def _search(a, val, i, j):
    if i > j:
        return -1

    mid = math.floor((i + j) / 2)

    if a[mid] == val:
        return mid

    if a[i] <= a[mid]:
        'sorted case'
        if a[i] <= val <= a[mid]:
            return _search(a, val, i, mid - 1)
        return _search(a, val, mid + 1, j)

    if a[mid] <= val <= a[j]:
        return _search(a, val, mid + 1, j)
    return _search(a, val, i, mid - 1)


def search(a, val):
    return _search(a, val, 0, len(a) - 1)


'''
Answer #6
For Array 'a' and lookup value 'v'
Iterate over the 'a' with index increasing in exponential way until we find a value that is equal to 'v' or greater.
Then use binary search to to find the value.
'''


def lookup_only_get(a, val):
    import math
    i = exp = 0
    while True:
        try:
            if a[i] == val:
                return i
            elif a[i] < val:
                i = int(math.pow(2, exp))
                exp += 1
            else:
                break;
        except Exception:
            break;

    left = math.floor(i/2)
    right = i - 1
    while left <= right:
        mid = math.floor(left + (right - left) / 2)
        if a[mid] == val:
            return mid
        elif val < a[mid]:
            left = mid - 1
        else:
            right = mid + 1
    return -1


'''
Answer #11

Given matrix of size MxN
For every row, use binary search to look for the last index of a negative number 'i'.
i + 1 = number of negative numbers in the row.

The complexity for the search in the matrix would be O(m * log n)
'''


def find_index_of_last_negative_number(a):
    import math
    l = 0
    r = len(a) - 1
    while l <= r:
        mid = math.floor(l + (r - l) / 2)
        if a[mid + 1] >= 0 > a[mid]:
            return mid
        elif a[mid] < 0:
            l = mid + 1
        else:
            r = mid - 1
    return -1


'''THIRD ROUND'''

'''
Answer #13
'''


def get_longest_decreasing_subsequence(arr):
    m = n = a = b = 1
    longest = current = 1
    for i in range(1, len(arr)):
        if arr[i - 1] >= arr[i]:
            b += 1
        else:
            current = (b - a) + 1
            if longest < current:
                longest = current
                m, n = a, b
            a = b = i

    return m, n


'''Fourth Round'''

'''
Answer #17
Majority element
'''


def get_majority_element(a):
    cont = 1
    ele = 0
    for i in range(1, len(a)):
        if a[ele] == a[i]:
            cont += 1
        else:
            cont -= 1

        if cont == 0:
            ele = i
            cont = 1
    return a[ele]


'''Final Section
Answers progress in file: simmachines.ipynb

- Answer A. Top 10 users that have listened to 'The beatles'

['0033ee7378661b88b245b1f67cc622ff63a51061', '0c4541503dd8f5b067976f40edc09d8c2a2322a4', 
'0de2759e5b8d1abb6fb7604230c07970da79ee8e', '03e7b02c10f651675001a268c6aae38f1668cee2', 
'0954e77dc1dafca788709611f895d270cfdfa5c8', '0d9f98701431e4c005ab76a472c28a274c21b015', 
'0481c9623e27a7d3f236440261d77d7753353f21', '0715e4b972ab477545ea2093a91f7fcb71420c4d', 
'01e19917350af651576cba8c7b4158ce389ae319', '0c4e5f8252f31afbf7270c42ceedeec36e7b54e0']


-Answer B. The most popular band: 'the beatles'

-Answer C. N/A
'''


if __name__ == '__main__':
    #   print(search([25, 26, 29, 40, 45, 1, 3, 7, 11, 20], 3))
    #   print(lookup_only_get([1, 2,3, 4, 5, 6, 7, 8, 9, 10], 6))
    #   print(find_index_of_last_negative_number([-10, -4, -3, -2, -2, 3, 4, 5, 6, 7]))
    print(get_longest_decreasing_subsequence([2,3,5,8,11,12,11,10,9,8,17,19,20]))
