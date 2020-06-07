#!/usr/bin/python3
import yaml
from heapq import heappop, heappush

swap = 0

def heap_sort(array):
    heap = []
    for element in array:
        heappush(heap, element)

    ordered = []

    # While we have elements left in the heap
    while heap:
        ordered.append(heappop(heap))

    return ordered

with open('../list.yaml') as lst:
    lst = yaml.load(lst, Loader=yaml.FullLoader)['list']
    print("Unsorted List:")
    print(lst)                 # dump unsorted list
    print("Sorting steps:")
    lst = heap_sort(lst)       # sort the list
    print('Sorted List:')
    print(lst)                 # dump sorted list
    print("Swaps:")
    print(swap)
