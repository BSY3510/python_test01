def solution(s):
    answer = 0
    idx = 0
    while (True) :
        if (idx >= len(s)) :
            break
        
        same = 0
        diff = 0
        
        temp = s[idx:]
        start_char = s[idx]
        for w in temp :
            if (w == start_char) :
                same += 1
            else :
                diff += 1
                
            idx += 1
                
            if (same == diff) :
                break
            
        answer += 1
    
    return answer

s  = "aaabbaccccabba"
print(solution(s))