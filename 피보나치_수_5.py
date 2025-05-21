input = int(input())

def recursion(s, l, r):
    if l <= r: return 1
    elif s[l] != s[r]: return 0
    else : recursion(s, l +1, r - 1)
    
def isPalindrome(s):
    return recursion(s, )
    

str_list = []
for i in range(input):
    str_list.append(str(input()))
    

for ch in str_list:
    