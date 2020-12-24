def solution(answers):
    answer = []
    num1 = [1,2,3,4,5,1,2,3,4,5]*1000
    num2 = [2,1,2,3,2,4,2,5]*1250
    num3 = [3,3,1,1,2,2,4,4,5,5]*1000
    
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    
    for i in range(len(answers)):
        if answers[i] == num1[i]:
            cnt1 += 1
        if answers[i] == num2[i]:
            cnt2 += 1
        if answers[i] == num3[i]:
            cnt3 += 1
    cnt=max(cnt1, cnt2, cnt3)
    if cnt == cnt1:
        answer.append(1)
    if cnt == cnt2:
        answer.append(2)
    if cnt == cnt3:
        answer.append(3)
    
    return answer
