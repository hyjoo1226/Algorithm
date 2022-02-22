총 재생횟수, 플레이횟수와 고유번호를 나타내는 해시를 만든다.

배열들을 순회하며 해시를 초기화시킨다.
총 재생횟수를 기초로 장르들을 정렬한 후 순회한다.
```
def solution(genres, plays):
    answer = []
    playDict = {}
    d = {}

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        playDict[genre] = playDict.get(genre, 0) + play
        d[genre] = d.get(genre, []) + [ (play, i) ]

    genreSort = sorted(playDict.items(), key=lambda x: x[1], reverse=True)
    for genre, totalPlay in genreSort:
        d[genre] = sorted(d(genre), key=lambda x: (-x[0], x[1]))
        answer += [ idx for play, idx in d[genre][:2] ]
    return answer
```