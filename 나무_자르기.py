import sys
# sys.stdin = open('input.txt', 'r')

def binary_search(left, right):
        result = 0
        while left <= right:
            mid = (left + right) // 2
            
            remains = sum(tree - mid for tree in trees if tree >= mid)
            
            if remains < m:
                right = mid - 1
            else:
                result = mid
                left = mid +1

        return result
                
        
        
n, m = map(int, input().split())
trees = list(map(int, input().split()))


print(binary_search(0, max(trees)))
 