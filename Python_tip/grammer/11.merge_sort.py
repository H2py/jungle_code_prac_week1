def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    
    sorted_left = merge_sort(left_arr)
    sorted_right = merge_sort(right_arr)
    
    return merge(sorted_left, sorted_right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else :
            result.append(right[i])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result    
    

unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
sortedArr = merge_sort(unsortedArr)
print("Sorted Array:", sortedArr)