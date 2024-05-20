n = int(input())
left_sum = 0
right_sum = 0


for i in range(n):
    temp_int = int(input())
    left_sum += temp_int

for i in range(n):
    temp_int = int(input())
    right_sum += temp_int

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")

else:
    print(f"No, diff = {abs(left_sum - right_sum)}")
