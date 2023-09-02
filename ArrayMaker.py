def solution(arr, queries):
    answer = []
    for i in range(len(queries)) :
        temp = arr[queries[i][0]:queries[i][1]+1]
        num = queries[i][2]
        mini = -1
        for j in range(len(temp)) :
            if temp[j] > num and (mini > temp[j] or mini == -1):
                mini = temp[j]
        answer.append(mini)
    return answer

array = [0, 1, 2, 4, 3]
queries = [[0, 4, 2],[0, 3, 2],[0, 2, 2]]
print(solution(array, queries))
#result = [3, 4, -1]
