inp = int(input())
row = [0] * inp
cnt = 0

def is_used(i) :
    for j in range(i):
        if row[i] == row[j] or abs(row[i] - row[j]) == abs(i-j):
            return False
    return True

def n_queen(i):
    global cnt
    if i == inp:
        cnt +=1
        return 
    
    for j in range(inp):
        row[i] = j
        if is_used(i):
            n_queen(i+1)
            
n_queen(0)
print(cnt)