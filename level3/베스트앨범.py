def solution(genres, plays):
    answer = []
    song = {}
    song_sum = {}
    for i in range(len(genres)):
        if song.get(genres[i], 0) == 0:
            song[genres[i]] = [[plays[i],i]]
            song_sum[genres[i]] = plays[i]
        else:
            song[genres[i]].append([plays[i],i])
            song_sum[genres[i]] += plays[i]
    song_sum = sorted(song_sum.items(), key = lambda x: x[1] , reverse=True)
    for g, _ in song_sum:
        so = song[g]
        so = sorted(so, key = lambda x: x[0], reverse=True)
        cnt = 0
        for i in so:
            if cnt == 2:
                break
            answer.append(i[1])
            cnt += 1
    return answer
