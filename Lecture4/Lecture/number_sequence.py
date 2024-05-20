n = int(input())

temp_int = int(input())
min = temp_int
max = temp_int

for i in range(n - 1):
    temp_int = int(input())
    if temp_int > max:
        max = temp_int
    if temp_int < min:
        min = temp_int

print(f"Max number: {max}")
print(f"Min number: {min}")