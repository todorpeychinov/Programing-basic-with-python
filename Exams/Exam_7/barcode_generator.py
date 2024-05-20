n1 = input()
n2 = input()



for i in range(int(n1[0]), int(n2[0]) + 1):
    if i % 2 == 0:
        continue
    for j in range(int(n1[1]), int(n2[1]) + 1):
        if j % 2 == 0:
            continue
        for k in range(int(n1[2]), int(n2[2]) + 1):
            if k % 2 == 0:
                continue
            for m in range(int(n1[3]), int(n2[3]) + 1):
                if m % 2 == 0:
                    continue
                print(f"{i}{j}{k}{m}", end=" ")
