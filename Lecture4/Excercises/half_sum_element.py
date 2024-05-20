import sys

n = int(input())

max_num = -sys.maxsize
sum = 0

for i in range(n):
    num = int(input())
    sum += num
    if num > max_num:
        max_num = num

if max_num == sum - max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    print("No")
    sum_other = max_num - (sum - max_num)
    print(f"Diff = {abs(sum_other)}")