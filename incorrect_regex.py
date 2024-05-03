# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
t = int(input())
for _ in range(t):
    regex = input()
    
    if any(op + '+' in regex for op in ['*', '+', '?']):
        print("False")
    else:
        try:
            re.compile(regex)
            print("True")
        except re.error:
            print("False")