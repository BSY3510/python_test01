def solution(chicken):
    answer = 0
    coupon = 0
    c = chicken
    eat = 0
    while c >= 0 :
        if eat == 10 :
            answer += 1
            c += 1
            eat = 1
            c -= 1
        else :
            c -= 1
            eat += 1
    return answer

chicken = 100
print(solution(chicken))
#result = 11

chicken = 1081
print(solution(chicken))
#result = 120
