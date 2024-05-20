student_tickets = 0
kids_tickets = 0
standard_tickets = 0

while True:
    movie_name = input()
    if movie_name == "Finish":
        break

    capacity = int(input())
    filled_places = 0

    while capacity > filled_places:
        ticket_type = input()

        if ticket_type == "End":
            break
        elif ticket_type == "student":
            student_tickets += 1
            filled_places += 1
        elif ticket_type == "standard":
            standard_tickets += 1
            filled_places += 1
        elif ticket_type == "kid":
            kids_tickets += 1
            filled_places += 1

    print(f"{movie_name} - {filled_places / capacity * 100:.2f}% full.")

total_tickets = standard_tickets + student_tickets + kids_tickets

print(f"Total tickets: {total_tickets}")
print(f"{student_tickets / total_tickets * 100:.2f}% student tickets.")
print(f"{standard_tickets / total_tickets * 100:.2f}% standard tickets.")
print(f"{kids_tickets / total_tickets * 100:.2f}% kids tickets.")

