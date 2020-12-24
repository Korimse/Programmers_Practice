def solution(n, lost, reserve):
    answer = 0
    num = []
    for i in range(n):
        num.append(1)
    for i in reserve:
        num[i-1] = 2
    for i in lost:
        num[i-1] -= 1
    
    for i in range(len(num)):
        if num[i] == 0:
            if i > 0 and num[i-1] == 2:
                num[i] = 1
                num[i-1] = 1
            elif i < n-1 and num[i+1] == 2:
                num[i] = 1
                num[i+1] = 1
    for i in range(len(num)):
        if num[i] >= 1:
            answer += 1
    return answer
