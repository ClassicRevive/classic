# Merge sort implementation

import math

def mergesort(arr):
    # base case, single element array
    if len(arr) < 2:
        return

    # create left and right lists and call merge sort recursively
    mid = len(arr) // 2
    L = arr[:mid]
    R = arr[mid:]

    mergesort(L)
    mergesort(R)

    # merging process
    i = j = k = 0

    # merging the left and right splits
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # finish merging the splits
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

def main():
    arr = [32, 12, 4, 8, 1000, 999]
    mergesort(arr)
    print(arr)
if __name__ == '__main__':
    main()