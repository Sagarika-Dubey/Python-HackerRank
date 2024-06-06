# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
S = input()
k = f"(?={input()})"
length = len(k) - 4
for m in re.finditer(k, S):
    print(f"({m.start()}, {m.start() + length -1})")
if not re.search(k, S):
    print("(-1, -1)")