def solution(n) :
    answer = [[0] * n for _ in range(n)]
    
    count = 1
    x = 0
    y = 0
    direction = 0       # 0: right, 1: down, 2: left, 3: up
    print(count, n*n)
    while (count <= n*n) :
        if (answer[x][y] == 0) :
            answer[x][y] = count
            count += 1
        if (direction == 0) :
            y += 1
        elif (direction == 1) :
            x += 1
        elif (direction == 2) :
            y -= 1
        else :
            x -= 1
        
        if (x >= n) :
            direction = 2
            x -= 1
        elif (x < 0) :
            direction = 0
            x += 1
        elif (y >= n) :
            direction = 1
            y -= 1
        elif (y < 0) :
            direction = 3
            y += 1 
        elif (direction == 0 and answer[x][y] != 0) :
            y -= 1
            direction = 1
        elif (direction == 1 and answer[x][y] != 0) :
            x -= 1
            direction = 2
        elif (direction == 2 and answer[x][y] != 0) :
            y += 1
            direction = 3
        elif (direction == 3 and answer[x][y] != 0) :
            x += 1
            direction = 0
        
    return answer

n = 4
print(solution(n))