def solution(numbers, hand):
    answer = ''
    button = [1,2,3,4,5,6,7,8,9,"*",0,"#"]
    L_index = (3, 0)
    R_index = (3, 2)
    L_range = [1,4,7]
    R_range = [3,6,9]
    
    for number in numbers :
        temp = button.index(number)
        temp_row = temp//3
        temp_column = temp%3
        if (number in L_range) :
            L_index = (temp_row, temp_column)
            answer += "L"
        elif (number in R_range) :
            R_index = (temp_row, temp_column)
            answer += "R"
        else :
            L_dist = abs(temp_row - L_index[0]) + abs(temp_column - L_index[1])
            R_dist = abs(temp_row - R_index[0]) + abs(temp_column - R_index[1])
            if (L_dist < R_dist) :
                L_index = (temp_row, temp_column)
                answer += "L"
            elif (L_dist > R_dist) :
                R_index = (temp_row, temp_column)
                answer += "R"
            else :
                if (hand == "right") :
                    R_index = (temp_row, temp_column)
                    answer += "R"
                elif (hand == "left") :
                    L_index = (temp_row, temp_column)
                    answer += "L"

    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers, hand))