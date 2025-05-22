from typing import MutableSequence


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:] 
    
    sortedLeft = merge_sort(leftHalf)
    sortedRight = merge_sort(rightHalf)
    
    return merge(sortedLeft, sortedRight)   

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left)