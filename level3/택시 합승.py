def solution(n, s, a, b, fares):
    answer = 0
    INF = 109876543
    answer = INF
    
    dist = [[INF for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        dist[i][i] = 0
    for ss, e, w in fares:
        dist[ss][e] = w
        dist[e][ss] = w
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    for i in range(1, n+1):
        answer = min(answer, dist[s][i] + dist[i][a] + dist[i][b])
    return answer
