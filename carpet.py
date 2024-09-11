def solution(brown, yellow):
    width = 0       # width >= height
    height = 0
    answer = [width, height]
    
    for i in range(1, yellow+1) :
        if (yellow % i == 0) :
            y_w = yellow//i
            y_h = i
            
            temp = 1
            temp_b = (y_w+temp + y_h+temp)*2
            b = temp_b
            while (brown > b) :
                temp += 1
                temp_b = (y_w+temp + y_h+temp)*2
                b += temp_b
                
            if (b == brown) :
                answer = [max(y_w+temp+1, y_h+temp+1), min(y_w+temp+1, y_h+temp+1)]
    
    return answer

brown = 24
yellow = 24
print(solution(brown, yellow))