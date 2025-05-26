N, K = map(int, input().split())

queue = [x for x in range(1, N+1)]
result = []

while queue:
    for i in range(K):
        temp = queue.pop(0)  
        if i == K-1:  
            result.append(temp) 
        else:
            queue.append(temp)  

output = '<' + ', '.join(map(str, result)) + '>'
print(output)