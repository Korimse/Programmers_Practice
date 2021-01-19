from collections import deque


def bfs(computers, net, visited):
    queue = deque()
    queue.append(net)
    visited[net] = 1
    while queue:
        v = queue.popleft()
        for k in computers[v]:
            if visited[k] == 0:
                queue.append(k)
                visited[k] = 1

def solution(n, computers):
    answer = 0
    visited = [0]*(n+1)
    graph = [[] for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                graph[i+1].append(j+1)
    for i in range(1, n+1):
        if visited[i] == 0:
            bfs(graph, i, visited)
            answer += 1
    return answer