def solution(score):
    answer = []
    temp = []
    for i in range(len(score)) :
        e = score[i][0]
        m = score[i][1]
        aver = (e+m)/2
        temp.append([aver,i+1, 0])
    temp.sort(reverse=True, key=lambda x:x[0])
    grade = 1
    stack = 0
    temp[0][2] = grade
    if len(temp) > 1 :
        for i in range(1, len(temp)) :
            if temp[i-1][0] == temp[i][0] :
                temp[i][2] = grade
                stack += 1
            else :
                grade += stack+1
                temp[i][2] = grade
                stack = 0
    temp.sort(key=lambda x:x[1])
    for i in range(len(temp)) :
        answer.append(temp[i][2])
    return answer

score =[[80, 70], [90, 50], [40, 70], [50, 80]]
print(solution(score))
#result = [1, 2, 4, 3]

score =[[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]
print(solution(score))
#result = [4, 4, 6, 2, 2, 1, 7]
