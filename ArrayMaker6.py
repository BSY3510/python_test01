def solution(arr):
    answer = []
    indx = 0
    for i in range(len(arr)) :
        if not answer :
            answer.append(arr[i])
            indx = 0
        elif answer[indx] == arr[i] :
            answer.pop(indx)
            indx = indx-1
        else :
            answer.append(arr[i])
            indx += 1
    if not answer :
        return [-1]
    return answer

arr =[0, 1, 1, 1, 0]
print(solution(arr))
#result =[0, 1, 0]

arr =[0, 1, 0, 1, 0]
print(solution(arr))
#result =[0, 1, 0, 1, 0]

arr =[0, 1, 1, 0]
print(solution(arr))
#result = [-1]
