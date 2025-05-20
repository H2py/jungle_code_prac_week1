def solution(str):
    vowel = ['a', 'e', 'i', 'o', 'u']
    for v in vowel:
        str = str.replace(v, '')
    return str

print(solution('nice to meet you'))