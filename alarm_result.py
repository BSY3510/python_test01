def solution(id_list, report, k):
    answer = []
    graph = dict()
    for id in id_list :
        graph[id] = dict()
    
    for info in report :
        a, b = info.split(" ")
        if b not in graph[a] :
            graph[a][b] = 1
    result = dict()
    for id in id_list :
        result[id] = 0
        for key, v in graph.items() :
            if id in v.keys() :
                result[id] += 1
                
    valid_id = []
    for key, v in result.items() :
        if v >= k :
            valid_id.append(key)
    
    for key, v in graph.items() :
        count = 0
        for value in v.keys() :
            if value in valid_id :
                count += 1
        answer.append(count)
    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

print(solution(id_list, report, k))