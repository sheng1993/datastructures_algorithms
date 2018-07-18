"""
Given a sorted array of n distinct integers where each integer 
is in the range from 0 to m-1 and m > n. Find the smallest number that is missing from the array.
"""

def findFirstMissing(array, start, end):
 
    if (start > end):
        return end + 1
 
    if (start != array[start]):
        return start
 
    mid = int((start + end) / 2)
 
    # Left half has all elements
    # from 0 to mid
    if (array[mid] == mid):
        return findFirstMissing(array,
                          mid+1, end)
 
    return findFirstMissing(array, 
                          start, mid)

arr = [1,2,3,6,9]
n = len(arr)
print("Smallest missing element is",
      findFirstMissing(arr, 0, n-1))