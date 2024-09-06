def solution(today, terms, privacies):
    answer = []
    year, month, day = map(int, today.split("."))

    info = dict()
    for term in terms :
        type, period = term.split(" ")
        info[type] = int(period)

    limited = dict()
    for k, v in info.items() :
        temp_year = year
        temp_month = month
        temp_day = day
        y = v//12
        m = v%12
        if (temp_month - m <= 0) :
            temp_year -= y+1
            temp_month = temp_month - m + 12
        else :
            temp_month = temp_month - m
            temp_year -= y
            
        if (temp_day == 28) :
            if (temp_month == 12) :
                temp_year += 1
                temp_month = 1
                temp_day = 1
            else :
                temp_month += 1
                temp_day = 1
        else :
            temp_day += 1
            
        limited[k] = [temp_year, temp_month, temp_day]
    
    for idx, privacie in enumerate(privacies, 1) :
        p_info, p_type = privacie.split(" ")
        p_year, p_month, p_day = map(int, p_info.split("."))
        t_year, t_month, t_day = limited[p_type]

        if (p_year < t_year) :
            answer.append(idx)
        elif (p_year == t_year) :
            if (p_month < t_month) :
                answer.append(idx)
            elif (p_month == t_month) :
                if (p_day < t_day) :
                    answer.append(idx)
    return answer

today = "2020.04.16"
terms = ["A 36", "S 4"]
privacies = ["2017.04.17 A", "2014.04.16 S"]

print(solution(today, terms, privacies))