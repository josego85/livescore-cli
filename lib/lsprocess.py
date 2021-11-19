#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import enum
import os

'''
    module: containing all the backend processes
'''

def clear_screen():
    os.system('clear')

def find_longest_no(array):
    longest_length = 5
    for data in array:
        n = len(data)
        if n > longest_length:
            longest_length = n
    return longest_length

def flatten(arr):
    if isinstance(arr, list):
        for sub in arr:
            yield from flatten(sub)
    else:
        yield arr


# ['November 20', ['12:30', ['Leicester City', ['?', '-', '?'], 'Chelsea']]]
def get_longest_list(arr):
    n = 7
    list_to_return = [0] * 7
    for a in arr:
        if not isinstance(a, list):
            if len(a) > list_to_return[0]:
                list_to_return[0] = len(a)
        else:
            for i, each in enumerate(flatten(a)):
                if len(each) > list_to_return[(i%n)+1]:
                    list_to_return[(i%n)+1] = len(each)
    return list_to_return


def get_longest_list_table(arr):
    n = 10
    list_to_return = [0] * 10
    list_to_return[0] = 2

    for k, row in enumerate(arr[0][1]):
        if k != 0:
            for l, row_elem in enumerate(row):
                if l != 0:
                    if len(row_elem) > list_to_return[l]:
                        list_to_return[l] = len(row_elem)
    
    return list_to_return

# def get_longest_list(array):
#     list2return = [0]*len(array[0])
#     for row in array:
#         row_length = len(row)
#         if isinstance(row, list) is False:
#             if row_length > list2return[0]:
#                 list2return[0] = row_length
#         else:
#             for i in range(row_length):
#                 val = row[i]
#                 if isinstance(row[i], list) is True:
#                     val = row[i][0]
#                 row_row_length = len(val.strip())
#                 if row_row_length > list2return[i+1]:
#                     list2return[i+1] = row_row_length

#     return list2return
