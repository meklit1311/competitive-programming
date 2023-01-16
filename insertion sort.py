#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    m=arr[-1]
    for i in range(len(arr)-1,-1,-1):
        if arr[i]<arr[i-1] and i!=0:
            arr[i]=arr[i-1]
            for item in arr:
                print(item,end=" ")
            print()
            arr[i-1]=m
            
        else:
            for item in arr:
                print(item,end=" ")
            break

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
