import sys

mul = 1
for _ in range(3):
    input = int(sys.stdin.readline())
    mul *= input

seq_dict = {e: 0 for e in range(0,10)}
for str in str(mul):
    seq_dict[int(str)] += 1
    
for v in dict.values(seq_dict):
    print(v)