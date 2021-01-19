def solution(routes):
    answer = 0
    routes = sorted(routes, key = lambda x:x[1])
    camera = [0]*len(routes)
    for i in range(len(routes)):
        if camera[i] == 1:
            continue
        cam = routes[i][1]
        answer += 1
        for j in range(i, len(routes)):
            if routes[j][0] <= cam <= routes[j][1]:
                camera[j] = True
    return answer