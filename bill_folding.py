def solution(wallet, bill):
    answer = 0
    w_height = wallet[1]
    w_width = wallet[0]
    t_height = bill[1]
    t_width = bill[0]
    while (True) :
        if (w_height >= t_height and w_width >= t_width) :
            break
        elif (w_height >= t_width and w_width >= t_height) :
            break
        
        if (t_height > t_width) :
            t_height = t_height // 2
        else :
            t_width = t_width // 2
            
        answer += 1

    return answer

wallet = [50,50]
bill = [100, 241]
print(solution(wallet, bill))