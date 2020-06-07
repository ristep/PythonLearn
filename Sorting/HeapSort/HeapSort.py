#!/usr/bin/python3
import yaml

swap = 0


def heapify(arr, n, i):
    global swap
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        swap, arr[i], arr[largest] = swap+1, arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(arr):
    global swap
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        swap, arr[i], arr[0] = swap+1, arr[0], arr[i]
        heapify(arr, n, i)


with open('../list.yaml') as lst:
    lst = yaml.load(lst, Loader=yaml.FullLoader)['list']
    print("Unsorted List:")
    print(lst)                 # dump unsorted list
    print("Sorting steps:")
    heapSort(lst)              # sort the list
    print('Sorted List:')
    print(lst)                 # dump sorted list
    print("Swaps:")
    print(swap)
