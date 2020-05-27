#!/usr/bin/python3
import yaml

def bubble_sort(ls):
    lenl = len(ls)
    iter = 0
    hswap = True        # Has swaped
    while(hswap):       # Walkthrough the list, until the last element
        hswap = False
        for j in range(lenl - (iter + 1)): 
            if ls[j] > ls[j+1]:
                ls[j], ls[j+1], hswap = ls[j+1], ls[j], True # Swaping elemets
        iter += 1        
        if hswap:
            print('{0:4d} {1}'.format(iter, ls))   # Print after the pass of a list.


with open('list.yaml') as lst:
    lst = yaml.load(lst, Loader=yaml.FullLoader)['list']
    print("Unsorted List:")
    print (lst)            # dump unsorted list 
    print("Sorting steps:")
    bubble_sort(lst)       # sort the list 
    print('Sorted List:')
    print (lst) # dump sorted list