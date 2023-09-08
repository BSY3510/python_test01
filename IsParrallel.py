def solution(dots):
    answer = 0
    s = []
    case1_1 = (dots[1][0]-dots[0][0])/(dots[1][1]-dots[0][1])
    case1_2 = (dots[3][0]-dots[2][0])/(dots[3][1]-dots[2][1])
    if abs(case1_1) == abs(case1_2) :
        return 1
    case2_1 = (dots[2][0]-dots[0][0])/(dots[2][1]-dots[0][1])
    case2_2 = (dots[3][0]-dots[1][0])/(dots[3][1]-dots[1][1])
    if abs(case2_1) == abs(case2_2) :
        return 1
    return answer

dots =[[1, 4], [9, 2], [3, 8], [11, 6]]
print(solution(dots))
#result = 1

dots =[[3, 5], [4, 1], [2, 4], [5, 10]]
print(solution(dots))
#result =0
