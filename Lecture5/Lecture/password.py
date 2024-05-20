username = input()
password = input()
user_input = ""

while user_input != password:
    user_input = input()

print(f"Welcome {username}!")