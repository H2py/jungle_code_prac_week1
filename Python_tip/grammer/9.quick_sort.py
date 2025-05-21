from typing import MutableSequence


a = [5,7,1,4,6,2,3,9,8]

def quick_sort(a: MutableSequence, left : int, right : int ) -> None:
    pl = left
    pr = right
    pivot = a[(left + right) // 2]
    
    while pl <= pr:
        while a[pl] < pivot : pl +=1
        while a[pr] > pivot : pr -=1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl +=1
            pr -=1
            
    if left < pr : quick_sort(a, left, pr)
    if right > pl: quick_sort(a, pl, right)
    

        