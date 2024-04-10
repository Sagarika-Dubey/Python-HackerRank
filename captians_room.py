from collections import Counter
k = int(input())
room_list = list(map(int, input().split(" ")))  
rooms = Counter(room_list)
for key, val in enumerate(rooms.items()):
    if val[1] == 1:
        print(val[0])