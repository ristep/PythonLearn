#!/usr/bin/python3
import yaml

# The simple implementation of Bubble Sort
def bubble_sort(ls):
    for i in range(len(ls)):          # Walkthrough the list, until the last element
        for j in range(len(ls) - 1):  # The last pair of elements will be (n-2, n-1)
            if ls[j] > ls[j+1]:
                ls[j], ls[j+1] = ls[j+1], ls[j] # Swaping elemets
        print(ls)  # Print after the pass of a list.


with open('list.yaml') as lst:
    lst = yaml.load(lst, Loader=yaml.FullLoader)['list']
    print (yaml.dump(lst)) # dump unsorted list 
    bubble_sort(lst)       # sort the list 
    print('Sorted List')
    print (yaml.dump(lst)) # dump sorted list

# bubble_sort(lst)
