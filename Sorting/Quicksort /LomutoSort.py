#!/usr/bin/python3
import yaml

swaps = 0

def quicksort(A, lo, hi):
    if(lo < hi):
        part = partition(A, lo, hi)
        quicksort(A, lo, part - 1)
        quicksort(A, part + 1, hi)

def partition(A, lo, hi):
    global swaps
    pivot = A[hi]
    i = lo
    j = lo
    while(j < hi):
        if(A[j] < pivot):
            A[i], A[j], swaps = A[j], A[i], swaps+1
            i = i + 1
        j = j + 1
    A[i], A[hi], swaps = A[hi], A[i], swaps+1
    return i

with open('../list.yaml') as lst:
    lst = yaml.load(lst, Loader=yaml.FullLoader)['list']
    print ("Unsorted List:")
    print (lst)                 # dump unsorted list 
    print ("Sorting steps:")
    quicksort(lst, 0, len(lst)-1 )       # sort the list 
    print ('Sorted List:')
    print (lst)                 # dump sorted list    
    print ( "Swaps:" )
    print ( swaps )