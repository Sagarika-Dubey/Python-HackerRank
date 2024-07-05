import re

NoOfInput = int(input())

for i in range(NoOfInput):
  MobileNo = input()
  pattern = (re.match(r"^[789]\d{9}$", MobileNo))
  if pattern:
    print("YES")
  else:
    print("NO")