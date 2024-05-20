import re

T = int(input())
N = []

for _ in range(T):
    N.append(input())

for n in N:
    try:
        float(n)
    except:
        print(False)
    else:
        if re.search(r"\+",n) and not(re.search(r"\d\+",n)):
            print(True)
        elif re.search(r"\-",n) and not(re.search(r"\d\-",n)):
            print(True)
        elif re.search(r"\.",n) and len(re.findall(r"\.",n))==1:
            print(True)
        else:
            print(False)