#Print("enter no of games:")
G= int(input())
Gid= []
for n in range(0, G):
    Gid.append(int(input()) )
#print("enter no of players:")
P=int(input())
Pid=[]
for q in range(0, P):
    Pid.append(int(input())
i=.                      # wrong unable to group.
date=input("Enter date in YYYY-MM-DD format : ")
amount=int(input())
dataset = {
    'Game_id' : 'Gid[]',
    'player_id' : 'Pid[]',
    'unique_id' : 'set(player_id)',
    'unique_count': 'unique_id',
    'age' : '[enddate[i]-date[i]]',       ## wrong could understand how to take date (enddate ,date)  # Had thought of grouping i with player_id and game_id but i couldn't get how to group
    'cumulative_revenue' : '[age[i]*amount, age[i+1]*amount] '    ## wrong
}
print('Game_id' in dataset.values())
print('unique_count' in dataset.values())
print('age' in dataset.values())
print('cumulative_revenue' in dataset.values())