from collections import Counter

mylist = []

for i in range (int(input())):
    mylist.append(input())
    
count = Counter(mylist)

print(len(count.keys()))
print(' '.join(list(map(str,list(count.values())))))
