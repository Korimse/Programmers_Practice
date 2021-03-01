def check(s):
    if s == s[::-1]:
        return True
    else:
        return False
def solution(s):
    maxv = -1
    for i in range(len(s)):
        for j in range(i, len(s)+1):
            if check(s[i:j]):
                maxv = max(maxv, len(s[i:j]))

    return maxv
