def ejin(x, n):
    s = ""
    for i in range(n):
        s = str(x%2)+s
        x //= 2
    return s
def solution(n, arr1, arr2):
    answer = ["" for _ in range(n)]
    count = 0
    for i, j in zip(arr1, arr2):
        a, b = ejin(i, n), ejin(j, n)
        for k in range(n):
            if a[k] == '1' or b[k] == '1':
                answer[count] += "#"
            elif a[k] == '0' and b[k] == '0':
                answer[count] += ' '
        count+=1
    return answer