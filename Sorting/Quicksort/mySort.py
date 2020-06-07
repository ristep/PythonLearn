#!/usr/bin/python3
import yaml

swap = 0

def quicksort(A, lo, hi):
    if lo < hi:
        parti = partition(A, lo, hi)
        quicksort(A, lo, parti )
        quicksort(A, parti + 1, hi)

def partition(A, lo, hi):
    global swap
    i, j = lo, hi
    pivot = A[(hi + lo) // 2]
    while i < j :
        while A[i] < pivot : i += 1
        while A[j] > pivot : j -= 1
        if i >= j  : return j
        if A[i] > A[j] :
            print("Swap {} {}".format(A[i],A[j]))
            print(A)
            swap, A[i], A[j] = swap+1, A[j], A[i]
        i += 1
        j -= 1
    return j    

with open('../list.yaml') as lst:
    lst = yaml.load(lst, Loader=yaml.FullLoader)['list']
    print ("Unsorted List:")
    print (lst)                 # dump unsorted list 
    print ("Sorting steps:")
    quicksort(lst, 0, len(lst)-1 )       # sort the list 
    print ('Sorted List:')
    print (lst)                 # dump sorted list    
    print ( "Swaps:" )
    print ( swap )