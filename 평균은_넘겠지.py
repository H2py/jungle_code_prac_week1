test = int(input())

for _ in range(test):
    avg_list=[]
    sum = 0
    student_num = int(input())
    for _ in range(student_num):
        score = int(input())
        avg_list.append(score)
    for score in avg_list:
        sum += score
    avg_score = sum / student_num 