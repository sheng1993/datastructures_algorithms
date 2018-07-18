"""
A naive method to solve this problem is to search all positive integers, 
starting from 1 in the given array. We may have to search at most n+1 
numbers in the given array. So this solution takes O(n^2) in worst case.

We can use sorting to solve it in lesser time complexity. We can sort 
the array in O(nLogn) time. Once the array is sorted, then all we need 
to do is a linear scan of the array. So this approach takes O(nLogn + n) 
time which is O(nLogn).

We can also use hashing. We can build a hash table of all positive elements 
in the given array. Once the hash table is built. We can look in the hash 
table for all positive integers, starting from 1. As soon as we find a number 
which is not there in hash table, we return it. This approach may 
take O(n) time on average, but it requires O(n) extra space.
"""

def findMissing(arr: list):
    shift = segregate(arr)
    return findMissingPositive(arr, shift)

def findMissingPositive(arr: list, shift: int):
    for i in range(shift, len(arr)):
        arr_pos = abs(arr[i]) - 1 + shift
        if arr_pos < len(arr) and arr[arr_pos] > 0:
            arr[arr_pos] = -arr[arr_pos]
    
    for i in range(shift, len(arr)):
        if arr[i] > 0:
            return (i+1) - shift
    
    return len(arr) - shift + 1

def segregate(arr: list):
    j = 0
    for i in range(len(arr)):
        if arr[i] <= 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return j

print(findMissing([1, 2, 0]))