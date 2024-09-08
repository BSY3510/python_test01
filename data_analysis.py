def solution(data, ext, val_ext, sort_by):
    answer = []
    object_list = list()
    for info in data :
        temp_dict = dict()
        temp_dict["code"] = info[0]
        temp_dict["date"] = info[1]
        temp_dict["maximum"] = info[2]
        temp_dict["remain"] = info[3]
        object_list.append(temp_dict)
        
    filter_list = list()
    for object in object_list :
        if (object[ext] <= val_ext) :
            filter_list.append(object)
            
    filter_list.sort(key=lambda x : x[sort_by])
    
    for object in filter_list :
        temp_list = [object["code"], object["date"], object["maximum"], object["remain"]]
        answer.append(temp_list)
        
    return answer

data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
ext = "date"
val_ext = 20300501
sort_by = "remain"

print(solution(data, ext, val_ext, sort_by))