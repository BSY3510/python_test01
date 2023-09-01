def solution(arr):
    answer = [0, 0]
    n = len(arr)
    
    def quard(x, y, n) :
        first = arr[x][y]
        for i in range(x, x+n) :
            for j in range(y, y+n) :
                if arr[i][j] != first :
                    n = n // 2
                    quard(x, y, n)
                    quard(x, y+n, n)
                    quard(x+n, y, n)
                    quard(x+n, y+n, n)
                    return    
        answer[first] += 1
    quard(0,0,n)
    return answer

array = [[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]
answer = solution(array)
print(answer)
