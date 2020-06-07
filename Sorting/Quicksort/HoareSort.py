#!/usr/bin/python3
import yaml

swaps = 0

def quicksort(A, lo, hi):
    if lo < hi :
        partition_border = partition(A, lo, hi)
        quicksort(A, lo, partition_border)
        quicksort(A, partition_border + 1, hi)

def partition(A, lo, hi):
    global swaps
    pivot = A[(hi + lo) // 2]
    i = lo
    j = hi
    while True:
        while( A[i] < pivot ) : i = i + 1
        while( A[j] > pivot ) : j = j - 1
        if i >= j : return j
        A[i], A[j], swaps = A[j], A[i], swaps+1
        i = i + 1
        j = j - 1

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