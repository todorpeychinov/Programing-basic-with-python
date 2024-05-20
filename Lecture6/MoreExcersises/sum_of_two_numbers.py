beginning = int(input())
end = int(input())
magic_number = int(input())
is_found = False

counter = 0

for i in range(beginning, end + 1):
    for j in range(beginning, end + 1):
        counter += 1
        if i + j == magic_number:
            print(f"Combination N:{counter} ({i} + {j} = {magic_number})")
            is_found = True
            break
    if is_found:
        break
else:
    print(f"{counter} combinations - neither equals {magic_number}")