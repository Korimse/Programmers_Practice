def solution(dartResult):
    answer = []
    n = ''
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(len(dartResult)):
        if dartResult[i] in num:
            n += dartResult[i]
        if dartResult[i] == 'S':
            answer.append(int(n))
            n = ''
        elif dartResult[i] == 'D':
            answer.append(int(n)**2)
            n = ''
        elif dartResult[i] == 'T':
            answer.append(int(n)**3)
            n = ''
        elif dartResult[i] == '*':
            if len(answer) >= 2:
                answer[-2] *= 2
            answer[-1] *= 2
        elif dartResult[i] == '#':
            answer[-1] *= -1
    result = sum(answer)
    return result