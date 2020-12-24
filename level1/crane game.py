def solution(board, moves):
    answer = 0
    arr = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] == 0:
                continue
            else:
                arr.append(board[j][i-1])
                board[j][i-1] = 0
                for k in range(0, len(arr)-1):
                    if len(arr) >= 2 and arr[k] == arr[k+1]:
                        del arr[k]
                        del arr[k]
                        answer += 2
                break
    return answer
