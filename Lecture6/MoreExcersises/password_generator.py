n = int(input())
l = int(input())


for sym1 in range(1, n):
    for sym2 in range(1,n):
        for sym3 in range(ord('a'), ord('a') + l):
            for sym4 in range(ord('a'), ord('a') + l):
                for sym5 in range(1, n + 1):
                    if sym5 > sym1 and sym5 > sym2:
                        print(f"{sym1}{sym2}{chr(sym3)}{chr(sym4)}{sym5}", end=" ")

 