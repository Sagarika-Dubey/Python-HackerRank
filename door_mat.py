# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M =list(map(int, input().split()))
a=".|."

for i in range(N//2):
    print((a*(2*i+1)).center(M, "-"))
print("WELCOME".center(M, "-"))
for i in reversed(range(N//2)):
    print((a*(2*i+1)).center(M, "-"))