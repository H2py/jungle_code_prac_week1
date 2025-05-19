import sys
n = int(input())
words = list(set([sys.stdin.readline().strip() for _ in range(n)]))
words.sort()
print('\n'.join(sorted(words, key=len)))