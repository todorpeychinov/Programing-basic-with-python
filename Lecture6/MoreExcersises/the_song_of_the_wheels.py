control_number = int(input())
password = ""
counter = 0

for a in range(1,10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a * b + c * d == control_number and a < b and c > d:
                    counter += 1
                    print(f"{a}{b}{c}{d}", end=" ")
                    if counter == 4:
                        password = f"{a}{b}{c}{d}"

if password != "":
    print()
    print(f"Password: {password}")
else:
    print()
    print("No!")