searched_book = input()
user_input = ""
counter = 0

while True:
    user_input = input()
    if user_input == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {counter} books.")
        break
    if user_input == searched_book:
        print(f"You checked {counter} books and found it.")
        break
    counter += 1
