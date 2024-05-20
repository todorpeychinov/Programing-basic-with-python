n = int(input())
range_1 = n % 10 + 1
n //= 10
range_2 = n % 10 + 1
range_3 = n // 10 + 1


for i in range(1, range_1):
    for j in range(1, range_2):
        for k in range(1,range_3):
            print(f"{i} * {j} * {k} = {i * j * k};")