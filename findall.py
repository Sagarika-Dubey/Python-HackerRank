# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
pattern = r"(?<=[^aeiou])([aeiou|AEIOU]{2,})(?=[^aeiou])"
s = input()
match = list(map(lambda x: x.group(), re.finditer(pattern, s)))

if match:
    for i in match:
        print(i)
else:
    print(-1)
