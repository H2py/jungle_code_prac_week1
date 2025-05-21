def solution(my_strings, parts):
    answer = []
    for i, str in enumerate(my_strings):
        a,b = parts[i]
        answer.append(str[a:b+1])
    return ''.join(answer)