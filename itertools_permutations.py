# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
s,n = input().split()
n = int(n)
s = sorted(s)
a = list(permutations(s,n))
for i in a:
    print(''.join(i))