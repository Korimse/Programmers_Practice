import math
def solution(n, stations, w):
    result = 0
    distance = []
    
    for i in range(1, len(stations)):
        distance.append((stations[i]-w-1) - (stations[i-1]+w))

    distance.append(stations[0]-w-1)
    distance.append(n-(stations[-1]+w))
    for i in distance:
        if i <= 0:
            continue
        result += math.ceil(i/(w*2+1))
    return result
