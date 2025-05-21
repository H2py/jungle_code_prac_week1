import sys
# sys.stdin = open('input.txt', 'r')
input = int(input())

cnt = 0
def recursion(s, l, r):
    global cnt
    cnt +=1
    if l >= r:
        return 1
    elif s[l] != s[r]: 
        return 0
    else : 
        return recursion(s, l +1, r - 1)
    
def isPalindrome(s):
    global cnt
    cnt = 0
    return recursion(s, 0, len(s)-1)
    

str_list = []
for i in range(input):
    str_list.append(str(sys.stdin.readline().strip()))
    

for str in str_list:
    print("{0} {1}".format(isPalindrome(str), cnt))