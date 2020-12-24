def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        start, end, k = commands[i]
        ans = array[start-1:end]
        ans.sort()
        answer.append(ans[k-1])
    return answer
