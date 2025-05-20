def solution(arr, h):
    return sum(1 for v in arr if (v > h))