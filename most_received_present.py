def solution(friends, gifts):
    answer = 0
    
    graph = dict()
    for friend in friends :
        graph[friend] = dict()
        graph[friend]["rate"] = 0
        for other in friends :
            if other != friend :
                graph[friend][other] = 0
                
    for gift in gifts :
        A, B = gift.split(" ")      # A는 선물을 준 친구    B는 선물을 받은 친구
        graph[A][B] += 1
        graph[A]["rate"] += 1
        graph[B]["rate"] -= 1
                
    #print(graph)
    
    max_counter = 0
    for friend in friends :
        count = 0
        for other in friends :
            if friend != other :
                if graph[friend][other] > graph[other][friend] :
                    count += 1
                elif graph[friend][other] == graph[other][friend] :
                    if graph[friend]["rate"] > graph[other]["rate"] :
                        count += 1
        if count > max_counter :
            max_counter = count
    
    answer = max_counter
    return answer

friends = ["muzi", "ryan", "frodo", "neo"]
gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
print(solution(friends, gifts))