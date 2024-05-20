start = int(input())
stop = int(input())

for i in range(start, stop + 1):
    for j in range(start, stop + 1):
        for k in range(start, stop + 1):
            for l in range(start, stop + 1):
                if i % 2 == 0 and l % 2 != 0 and i > l and (j + k) % 2 == 0:
                    print(f"{i}{j}{k}{l}", end=" ")
                elif i % 2 != 0 and l % 2 == 0 and i > l and (j + k) % 2 == 0:
                    print(f"{i}{j}{k}{l}", end=" ")
