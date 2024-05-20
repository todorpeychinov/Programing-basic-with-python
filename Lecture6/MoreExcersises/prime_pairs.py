from math import sqrt

begin_1 = int(input())
begin_2 = int(input())
end_1 = int(input()) + begin_1 + 1
end_2 = int(input()) + begin_2 + 1

for i in range(begin_1, end_1):
    for j in range(begin_2, end_2):

        for k in range(2, int(sqrt(i)) + 1):
            if i % k == 0:
                break
        else:
            for m in range(2, int(sqrt(j)) + 1):
                if j % m == 0:
                    break
            else:
                print(f"{i}{j}")

