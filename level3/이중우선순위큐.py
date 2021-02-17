from collections import deque
import heapq

def solution(operations):
    answer = []
    result = []
    status = 1
    for operation in operations:
        a, b = operation.split(" ")
        if a == "I":
            heapq.heappush(result, int(b))
        elif a == "D":
            if len(result) == 0:
                continue
            if b == '1':
                maxv = max(result)
                for i in range(len(result)):
                    if result[i] == maxv:
                        del result[i]
                        break
            elif b == '-1':
                heapq.heappop(result)
    if len(result) == 0:
        return [0,0]
    return [max(result), min(result)]
            

    return answer
