standard = 0
student = 0
kid = 0
total = 0


while True:
    movie_name = input()

    if movie_name == "Finish":
        break
    capacity = int(input())
    people = 0

    while capacity > people:
        ticket_type = input()
        if ticket_type == "End":
            break
        elif ticket_type == "standard":
            standard += 1
        elif ticket_type == "student":
            student += 1
        elif ticket_type == "kid":
            kid += 1
        people += 1
        total += 1

    print(f"{movie_name} - {people / capacity * 100:.2f}% full.")

print(f"Total tickets: {total}")
print(f"{student / total * 100:.2f}% student tickets.")
print(f"{standard / total * 100:.2f}% standard tickets.")
print(f"{kid / total * 100:.2f}% kid tickets.")