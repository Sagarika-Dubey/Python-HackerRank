n=int(input())
a=set(list(map(int, input().split()))[::-1])
m=int(input())
for i in range(m):
    choice=input().split(" ")
    if (choice[0]=="pop"):
        a.pop()
    elif (choice[0]=="remove"):
        a.remove(int(choice[1]))
    elif (choice[0]=="discard"):
        a.discard(int(choice[1]))
    else:
        continue
print(sum(a))