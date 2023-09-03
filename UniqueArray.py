def solution(numlist, n):
    answer = []
    temp = numlist
    l = []
    for i in range(len(temp)) :
        t = temp[i] - n
        if t > 0 :
            l.append([temp[i], t])
        else :
            l.append([temp[i], (-t)+0.1])
    l.sort(key = lambda x : x[1])
    for i in range(len(l)) :
        answer.append(l[i][0])
    return answer

numlist =[1, 2, 3, 4, 5, 6]
n =4
print(solution(numlist, n))
# result =[4, 5, 3, 6, 2, 1]

numlist =[10000,20,36,47,40,6,10,7000]
n =30
print(solution(numlist, n))
# result = [36, 40, 20, 47, 10, 6, 7000, 10000]
