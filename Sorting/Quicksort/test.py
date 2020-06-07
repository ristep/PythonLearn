#!/usr/bin/python3
import yaml

swap = 0

def quicksort(arr, fst, lst):
    if fst < lst:
        split = parti(arr, fst, lst)
        quicksort(arr, fst, split)
        quicksort(arr, split+1, lst)

def parti(arr, fst, lst):
    global swap
    i, j = fst, lst
    pivot = arr[(fst+lst)//2]
    while i < j :
        while arr[i] < pivot : i += 1
        while arr[j] > pivot : j -= 1
        if i >= j  : return j
        if arr[i] > arr[j]:
          print("Swap {} {}".format(arr[i],arr[j]))
          print(arr)
          swap, arr[i], arr[j] = swap+1, arr[j], arr[i]
        i += 1
        j -= 1
    return j


with open('../list.yaml') as lst:
    lst = yaml.load(lst, Loader=yaml.FullLoader)['list']
    print("Unsorted List:")
    print(lst)                 # dump unsorted list
    print("Sorting steps:")
    quicksort(lst, 0, len(lst)-1)       # sort the list
    print('Sorted List:')
    print(lst)                 # dump sorted list
    print("Swaps:")
    print(swap)
