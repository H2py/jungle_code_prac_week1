def is_even(num):
    if num % 2 == 0:
        return True
    return False

def solution(num_list):
    answer=[]
    odd = 0
    even = 0
    for num in num_list:
        if is_even(num):
            even +=1
        else :
            odd +=1
    answer.append(even)
    answer.append(odd)
    return answer