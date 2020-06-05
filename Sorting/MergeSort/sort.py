#!/usr/bin/python3
import yaml

def merge(arrL, arrR):
    if len(arrL) == 0 : return arrL
    if len(arrR) == 0 : return arrR

    arrResult = []
    ndxL = ndxR = 0

    while len(arrResult) < len(arrL) + len(arrR):
        if arrL[ndxL] <= arrR[ndxR]:
            arrResult.append(arrL[ndxL])
            ndxL += 1
        else:
            arrResult.append(arrR[ndxR])
            ndxR += 1

        if ndxR == len(arrR):
            arrResult += arrL[ndxL:]
            break

        if ndxL == len(arrL):
            arrResult += arrR[ndxR:]
            break

    return arrResult

def merge_sort(array):
    if len(array) < 2 : return array
    midpoint = len(array) // 2
    return merge( arrL=merge_sort(array[:midpoint]), arrR=merge_sort(array[midpoint:]))


with open('../list.yaml') as lst:
    lst = yaml.load(lst, Loader=yaml.FullLoader)['list']
    print ("Unsorted List:")
    print (lst)                 # dump unsorted list 
    print ("Sorting steps:")
    lst = merge_sort(lst)       # sort the list 
    print ('Sorted List:')
    print (lst)                 # dump sorted list    