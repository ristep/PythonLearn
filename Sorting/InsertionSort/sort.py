#!/usr/bin/python3
import yaml

def insertion_sort(array):

    for i in range(1, len(array)):
        keyItem = array[i]         # current element
        j = i - 1

        while j >= 0 and array[j] > keyItem:
            array[j + 1], j = array[j], j-1

        array[j + 1] = keyItem
        print('{0:4d} {1} {2:5d}'.format(i, array, keyItem))


with open('../list.yaml') as lst:
    lst = yaml.load(lst, Loader=yaml.FullLoader)['list']
    print ("Unsorted List:")
    print (lst)                 # dump unsorted list 
    print ("Sorting steps:")
    insertion_sort(lst)         # sort the list 
    print ('Sorted List:')
    print (lst)                 # dump sorted list    