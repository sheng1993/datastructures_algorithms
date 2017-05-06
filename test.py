import sys
import math

def merge(A: list, B: list):
    global cont
    i = 0
    j = 0
    new_array = []

    while len(new_array) != len(A) + len(B):
        if i == len(A):
            new_array.append(B[j])
            j += 1
        elif j == len(B):
            new_array.append(A[i])
            i += 1
        elif A[i] <= B[j]:
            new_array.append(A[i])
            i += 1
        else:
            new_array.append(B[j])
            j+=1
            cont += (len(A) - i)

    return new_array


def merge_sort_cont(a):
    global cont

    if(len(a) == 1):
        return a

    m = math.floor(len(a)/2)
    B = merge_sort_cont(a[:m])
    C = merge_sort_cont(a[m:])
    A = merge(B,C)
    return A

if __name__ == '__main__':
    global cont
    cont = 0
    merge_sort_cont([5,4,3,2,1])
    print(cont)