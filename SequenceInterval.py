def solution(arr, queries):
    answer = arr
    for i in range(len(queries)) :
        start = queries[i][0]
        end = queries[i][1]
        num = queries[i][2]
        for j in range(start, end+1) :
            if j%num == 0 :
                answer[j] += 1
    return answer

array = [0, 1, 2, 4, 3]
queries = [[0, 4, 1],[0, 3, 2],[0, 3, 3]]
print(solution(array, queries))
#result = [3, 2, 4, 6, 4]
