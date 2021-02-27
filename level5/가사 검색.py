from bisect import bisect_left, bisect_right
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

def solution(words, queries):
    answer = []
    arr = [[] for _ in range(10001)]
    rarr = [[] for _ in range(10001)]
    for word in words:
        arr[len(word)].append(word)
        rarr[len(word)].append(word[::-1])
        
    for i in range(10001):
        arr[i].sort()
        rarr[i].sort()
    
    for q in queries:
        if q[0] != '?':
            result = count_by_range(arr[len(q)], q.replace("?", "a"), q.replace("?", "z"))
            
        else:
            result = count_by_range(rarr[len(q)], q[::-1].replace("?", "a"), q[::-1].replace("?", "z"))
        answer.append(result)
    return answer
