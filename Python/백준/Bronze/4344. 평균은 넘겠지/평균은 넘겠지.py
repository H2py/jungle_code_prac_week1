import sys
# sys.stdin = open('input.txt', 'r')
test = int(input())

for _ in range(test):
    input_list = list(map(int, sys.stdin.readline().split()))
    student_num = input_list[0]
    
    score_list = input_list[1:]
    
    avg_score = sum(score_list) / student_num
    count = 0
    for score in score_list :
        if score > avg_score:
            count += 1
            
    print("{:.3f}%".format(float(count / student_num) * 100))