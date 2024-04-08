A = set(map(int, input().split()))
result = []
for i in range(int(input())):
    B = set(map(int, input().split()))
    result.append(A>B)
print(False if False in result else True)