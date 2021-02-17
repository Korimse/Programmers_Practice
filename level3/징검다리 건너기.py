def cal(stones, k, mid):
    tmp = 0
    for stone in stones:
        if stone - mid <= 0:
            tmp += 1
            if tmp == k:
                return False
        else:
            tmp = 0
    return True

def solution(stones, k):
    answer = 0
    left = 1
    right = max(stones)
    while left <= right:
        mid = (left+right)//2
        if cal(stones, k, mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    return answer + 1
