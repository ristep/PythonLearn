#!/usr/bin/python3
import yaml

def bubble_sort(array):
  n = len(array)
  for iter in range(n):
    sorted = True

    for j in range(n - iter - 1):
      if array[j] > array[j + 1]:
        array[j], array[j + 1] = array[j + 1], array[j]
        sorted = False

    if sorted:  break
    print('{0:4d} {1}'.format(iter, array))   # Print after the pass of a list.


with open('../list.yaml') as lst:
    lst = yaml.load(lst, Loader=yaml.FullLoader)['list']
    print("Unsorted List:")
    print (lst)            # dump unsorted list 
    print("Sorting steps:")
    bubble_sort(lst)       # sort the list 
    print('Sorted List:')
    print (lst) # dump sorted list    