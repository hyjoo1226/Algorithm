def solution(genres, plays):
    answer = []
    music_dict = {}
    len_m = len(genres)
    for i in range(len_m):
        music_dict[(genres[i], i)] = plays[i]

    genre = {}
    for key, value in music_dict.items():
        if key[0] not in genre:
            genre[key[0]] = value
        else:
            genre[key[0]] += value
    
    genre_list = list(genre.items())
    sort_list = sorted(genre_list, key=lambda x: x[1], reverse=True)

    for item in sort_list:
        temp = []
        for key, value in music_dict.items():
            if item[0] == key[0]:
                temp.append([key[1], value])
        sort_temp = sorted(temp, key=lambda x: x[1], reverse=True)
        if len(sort_temp) == 1:
            answer.append(sort_temp[0][0])
        else:
            answer.append(sort_temp[0][0])
            answer.append(sort_temp[1][0])
    
    return answer