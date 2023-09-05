def solution(quiz):
    answer = []
    for i in quiz :
        temp = i.split()
        r = int(temp[4])
        save = 0
        a = int(temp[0])
        b = int(temp[2])
        if temp[1] == "+" :
            save = a + b
        elif temp[1] == "-" :
            save = a - b
        if save == r :
            answer.append("O")
        else :
            answer.append("X")
            
    return answer

quiz =["3 - 4 = -3", "5 + 6 = 11"]
print(solution(quiz))
#result =["X", "O"]

quiz =["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]	
print(solution(quiz))
#result =["O", "O", "X", "O"]
