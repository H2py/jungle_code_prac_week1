from sys import stdin
# stdin = open('input.txt', 'r')

# -10 2 3 6 10
def find_card(arr, target, start, end, i):
    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] == target:
            finds_bool[i] = 1
            return
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None

n = int(input())
cards = list(map(int, stdin.readline().split()))
m = int(input())
finds = list(map(int, stdin.readline().split()))
finds_bool = [0] * m
cards.sort()

for i, find in enumerate(finds):
    find_card(cards, find, 0, n-1, i)
    
# print(*finds_bool)
print(' '.join(str(x) for x in finds_bool))
