th = 0
n, m = map(int, input().split())
happiness = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
# Convert input integers to sets
A_set = set(A)
B_set = set(B)
    
# Iterate through the array
for i in happiness:
    if i in A_set:
        th += 1  # Add 1 to happiness if num is in set A
    elif i in B_set:
        th -= 1  # Subtract 1 from happiness if num is in set B
    
print(th)
