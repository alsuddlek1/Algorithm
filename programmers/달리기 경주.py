def solution(players, callings):
    players_dic = {player: index for index, player in enumerate(players)}
    for calling in callings:
        print(calling)
        index = players_dic[calling]
        players_dic[calling] -= 1
        players_dic[players[index - 1]] += 1
        players[index - 1], players[index] = players[index], players[index - 1]

    return players

