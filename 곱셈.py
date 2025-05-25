A, B, C = map(int, input().split())

def divide(a, b):
    if b == 1:
        return a % C
    half = divide(a, b//2)
    if b % 2 == 0:
        return (half * half) % C
    else:
        return (half * half * A) % C

print(divide(A, B))    