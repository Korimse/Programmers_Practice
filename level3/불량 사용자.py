from itertools import permutations

def check(banned_id, user):
    for i in range(len(banned_id)):
        if len(banned_id[i]) != len(user[i]):
            return False
        for j in range(len(banned_id[i])):
            if banned_id[i][j] == '*':
                continue
            elif banned_id[i][j] != user[i][j]:
                return False
    return True

def solution(user_id, banned_id):
    answer = []
    for users in permutations(user_id, len(banned_id)):
        if check(banned_id, users):
            users = set(users)
            if users not in answer:
                answer.append(users)
    return len(answer)
