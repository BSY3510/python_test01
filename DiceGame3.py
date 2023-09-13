def solution(a, b, c, d):
    answer = 0
    l = [a,b,c,d]
    l.sort()
    s = set(l)
    if len(s) == 1 :
        answer = 1111 * l[0]
    elif l.count(l[1]) == 3 :
        temp = l
        num = l[1]
        temp.remove(num)
        temp.remove(num)
        temp.remove(num)
        answer = (10*num + temp[0])*(10*num + temp[0])
    elif len(s) == 2 and l.count(l[0]) == 2 :
        answer = (l[0]+l[2]) * abs(l[0]-l[2])
    elif len(s) == 3 :
        num = 0
        temp = l
        for i in range(4) :
            if l.count(l[i]) == 2 :
                num = l[i]
                break
        temp.remove(num)
        temp.remove(num)
        answer = temp[0] * temp[1]
    elif len(s) == 4 :
        answer = l[0]
    return answer

a, b, c, d = 2, 2, 2, 2
print(solution(a, b, c, d))
#result = 2222

a, b, c, d = 4, 1, 4, 4
print(solution(a, b, c, d))
#result = 1681

a, b, c, d = 6, 3, 3, 6
print(solution(a, b, c, d))
#result = 27

a, b, c, d = 2, 5, 2, 6
print(solution(a, b, c, d))
#result = 30

a, b, c, d = 6, 4, 2, 5
print(solution(a, b, c, d))
#result = 2
