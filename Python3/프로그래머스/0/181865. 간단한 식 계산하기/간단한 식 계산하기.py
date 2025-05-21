def solution(binomial):
    answer = 0
    for str in binomial:
        if '+' in str:
            answer = binomial.split('+')
            a, b = map(int,answer)
            answer = a + b
        elif '-' in str:
            answer = binomial.split('-')
            a,b = map(int, answer)
            answer = a - b
        elif '*' in str:
            answer = binomial.split('*')
            a,b = map(int, answer)
            answer = a * b
    return answer