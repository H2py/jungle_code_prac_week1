import sys
input = sys.stdin.readline

str_list = input().strip().split('-')
result = []

for row in str_list:
    temp = row.split('+')
    temp_list = []
    for v in temp:
        if v == '':
            continue
        else:
            temp_list.append(int(v))
    result.append(sum(temp_list))

total = 0

if result[0] == 0:
    total -= result[1]
    
    for v in result[2:]:
        total -= v
elif result[0] != 0 and len(result) == 1:
    print(result[0])
    sys.exit()
else:
    total += result[0]
    
    for v in result[1:]:
        total -= v

print(total)    
