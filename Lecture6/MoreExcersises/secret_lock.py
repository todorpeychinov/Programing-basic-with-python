from math import sqrt

hundreds = int(input())
tens = int(input())
ones = int(input())

for i in range(2, hundreds + 1, 2):
    for j in range(2, tens + 1):
        for m in range(2, int(sqrt(j)) + 1):
            if j % m == 0:
                break
        else:
            for k in range(2, ones + 1, 2):
                print(i,j,k)
