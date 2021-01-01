def solution(a, b):
    answer = ''
    cnt = b
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    date = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    for i in range(a-1):
        cnt += month[i]
    answer = date[cnt%7-1]
    return answer
