import sys
a = int(sys.stdin.readline())

if a >= 90: print('A')
elif a >= 80 : print('B')
elif a >= 70 : print('C')
elif a >= 60 : print('D')
else : print('F')

#Why below code cannot run correctly?

if a >= 90:
    print('A')
elif a >= 80 and a<=89:
    print('B')
elif a>=70 and a<=79:
    print('C')
elif a>=60 and a<=69:
    print('D')
else: print('F')
    