import datetime
dataset_dict = {
    "game1": [("player1", "2021-01-01", 100), ("player2", "2021-01-01", 150), ("player1", "2021-01-10", 50)],
    "game2": [("player2", "2021-01-10", 200), ("player1", "2021-01-10", 250), ("player3", "2021-01-11", 50)],
    "game3": [("player1", "2021-01-10", 300), ("player1", "2021-01-15", 350), ("player1", "2021-01-15", 50)]
}
for k in dataset_dict:
    player_set = set()
    player_date= []
    player_cumA = []
    Age=0
    #number_of_unique_Players = len(Player_set)
    arrElement=dataset_dict.get(k)
    for eachVal in arrElement:
        firstElement=eachVal[0]
        player_set.add(firstElement)
        secondElement=eachVal[1]
        player_date.append(secondElement)
        #thirdElement=eachVal[2]
        #player_cumA.append(thirdElement)
    print(k) 
    print(len(player_set))
    #print(player_date)
    #print(player_cumA)
    for x in range(1):
        firstEle=player_date[x]
        secoundEle=player_date[x+1]
        Age=Age+ [datetime.timedelta(secoundEle)-datetime.timedelta(firstEle)]
    print(Age)