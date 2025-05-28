import sys
input = sys.stdin.readline

n, wifi = map(int, input().split())
homes = sorted(list(int(input()) for _ in range(n)))
