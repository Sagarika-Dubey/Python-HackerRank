from math import degrees, atan2

ab, bc = float(input()), float(input())
print(str(round(degrees(atan2(ab, bc)))) + "\xb0")