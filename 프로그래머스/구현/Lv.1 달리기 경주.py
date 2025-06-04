def solution(players, callings):
    player_dict = {}
    len_p = len(players)
    for i in range(len_p):
        player_dict[players[i]] = i

    for call in callings:
        temp = player_dict[call]
        pre_player = players[temp-1]
        players[temp], players[temp-1] = players[temp-1], players[temp]
        player_dict[call] -= 1
        player_dict[pre_player] += 1
        
    # 시간초과
    # for call in callings:
    #     index = players.index(call)
    #     temp = players[index - 1]
    #     players[index - 1] = players[index]
    #     players[index] = temp
        
    return players