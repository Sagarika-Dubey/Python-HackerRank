# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
z = input()
n = abs(complex(z))
phi = cmath.phase(complex(z))
print(n)
print(phi)