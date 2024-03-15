# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
a=set()
for i in range(N):
    ch=input()
    a.add(ch)
    
print(len(a))