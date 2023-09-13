def solution(babbling):
    answer = 0
    temp = babbling
    speak = ["aya", "ye", "woo", "ma"]
    for i in range(len(temp)) :
        for j in range(len(speak)) :
            if speak[j] in temp[i] :
                temp[i] = temp[i].replace(speak[j], str(j))
    sor1 = []
    for i in temp :
        if i.isdigit() :
            sor1.append(i)
    sor2 = []
    n = 0
    for i in sor1 :
        n = 0
        for j in range(len(i)-1) :
            if i[j+1] == i[j] :
                break
            else :
                n += 1
        if n == len(i)-1 :
            answer += 1
        
    return answer

babbling = ["aya", "yee", "u", "maa"]
print(solution(babbling))
#result = 1

babbling = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]
print(solution(babbling))
#result = 2
