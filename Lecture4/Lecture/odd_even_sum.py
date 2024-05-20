n = int(input())
even_sum = 0
odd_sum = 0

for i in range(n):
    temp_int = int(input())
    if i % 2 == 0:
        even_sum += temp_int
    else:
        odd_sum += temp_int


if even_sum == odd_sum:
    print("Yes")
    print(f"Sum = {even_sum}")
else:
    print("No")
    print(f"Diff = {abs(odd_sum - even_sum)}")