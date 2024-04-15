from collections import defaultdict

n, m = map(int, input().split())
lst_m = []
d = defaultdict(list)
for i in range(n):
    d[str(input())].append(i+1)
for i in range(m):
    lst_m.append(str(input()))
for item in lst_m:
    if item in d.keys():
        print(*d[item])
    else:
        print(-1)