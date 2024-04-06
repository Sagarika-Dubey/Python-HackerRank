n = int(input())
for _ in range(n):
    _ = input()
    set_a = {int(a) for a in input().split(' ')}
    _ = input()
    set_b = {int(a) for a in input().split(' ')}
    print(set_a.issubset(set_b))