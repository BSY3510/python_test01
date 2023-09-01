def solution(code) :
    mode = 0
    answer = ""
    for i in range(len(code)) :
        if code[i] == "1" :
            if mode == 0 :
                mode = 1
            else :
                mode = 0
        else :
            if mode == 0 :
                if i%2 == 0 :
                    answer += code[i]
            else :
                if i%2 == 1 :
                    answer += code[i]
    if not answer :
        return "EMPTY"
    return answer

code =""
print(solution(code))
