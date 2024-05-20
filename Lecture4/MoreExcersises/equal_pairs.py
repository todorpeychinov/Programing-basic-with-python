n = int(input())

x1 = int(input())
x2 = int(input())

sum = x1 + x2
is_equal = True
diff = 0
max_diff = 0


for i in range(n - 1):
    x1 = int(input())
    x2 = int(input())
    if (x1 + x2) != sum:
        sum2 = x1 + x2
        is_equal = False
        diff = abs(sum2 - sum)
        sum = sum2
        if max_diff < diff:
            max_diff = diff


if is_equal:
    print(f"Yes, value={sum}")
else:
    print(f"No, maxdiff={abs(max_diff)}")
