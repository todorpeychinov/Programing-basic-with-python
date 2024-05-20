start = input()
stop = input()
letter = input()
counter = 0

for i in range(ord(start), ord(stop) + 1):
    for j in range(ord(start), ord(stop) + 1):
        for k in range(ord(start), ord(stop) + 1):
            if chr(i) == letter or chr(j) == letter or chr(k) == letter:
                continue
            print(f"{chr(i)}{chr(j)}{chr(k)}", end=" ")
            counter += 1

print(counter)



