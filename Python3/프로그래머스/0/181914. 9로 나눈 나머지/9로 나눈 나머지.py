def solution(number):
    sum = 0
    for ch in number:
        sum += int(ch)
    return sum % 9