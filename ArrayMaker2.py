def solution(l, r):
    answer = []
    for i in range(l, r+1) :
        temp = set(list(str(i)))
        if {'0'} == temp or {'0','5'} == temp or {'5'} == temp:
            answer.append(i)
            
    if len(answer) == 0 :
        answer.append(-1)
    return answer

l = 5
r = 555
print(solution(l,r))
#result = [5, 50, 55, 500, 505, 550, 555]

l = 10
r = 20
print(solution(l,r))
#result = [-1]
