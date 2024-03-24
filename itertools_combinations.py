from itertools import combinations
S, k = input().split(" ")
for i in range(int(k)):
    for i in combinations(sorted(S), i + 1):
        print("".join(i))