import numpy
[N, M, P] = list(map(int, input().split(" ")))

arrayN = []
arrayM = []

for i in range(N):
    arrayN.append(list(map(int, input().split(" "))))
for i in range(M):
    arrayM.append(list(map(int, input().split(" "))))

outputArr = numpy.concatenate((arrayN, arrayM))

print(outputArr)