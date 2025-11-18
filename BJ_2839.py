def solution():
    bags = [3, 5]
    N = int(input())
    answer = -1
    
    dp = [[bags[0]*x + bags[1]*y for x in range(N//bags[0]+1)] for y in range(N//bags[1]+1)]
    
    min_count = 1e9
    for row in dp:
        if N in row:
            count = row.index(N) + dp.index(row)
            min_count = min(min_count, count)
            answer = min_count
    
    return answer

print(solution())
