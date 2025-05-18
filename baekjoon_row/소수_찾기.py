import math

test = int(input())
input_list = list(map(int, input().split()))
count = 0

for num in input_list:
    if num == 1:
        continue
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            break    
    else:
        count += 1
        
print(count)