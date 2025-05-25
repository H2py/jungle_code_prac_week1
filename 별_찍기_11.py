import sys
sys.setrecursionlimit(10**6)
num = int(input())


def make_star(n):
    if n == 3:
        return ['  *  ', ' * * ', '*****']
    
    star = make_star(n//2)
    A = []
    
    if i in star:
        A.append(' '*(n//2)+i+' '*(n//2))
    for i in star:
        A.append(i+' '+i)    
    
    return A

        
print('\n'.join(make_star(num)))