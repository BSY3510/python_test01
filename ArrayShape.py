def solution(arr, query):
    answer = arr
    for i in range(len(query)) :
        indx = query[i]
        if i%2 == 0 :
            answer = answer[:indx+1]
        else :
            answer = answer[indx:]
    return answer

arr =[0, 1, 2, 3, 4, 5]
query = [4, 1, 2]
print(solution(arr, query))
#result = [1, 2, 3]
