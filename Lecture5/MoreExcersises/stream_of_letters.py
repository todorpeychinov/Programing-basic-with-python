counter_o = 0
counter_n = 0
counter_c = 0
user_output = ""

while True:
    user_input = input()

    if user_input == "End":
        break

    if (ord(user_input) >= 97 and ord(user_input) <= 122) or (ord(user_input) >= 65 and ord(user_input) <= 90):
        if user_input == 'c':
            if counter_c > 0:
                user_output += user_input
            else:
                counter_c += 1

        elif user_input == 'o':
            if counter_o > 0:
                user_output += user_input
            else:
                counter_o += 1

        elif user_input == 'n':
            if counter_n > 0:
                user_output += user_input
            else:
                counter_n += 1

        else:
            user_output += user_input

    if (counter_o > 0 and counter_c > 0 and counter_n > 0):
        print(user_output + " ", end="")
        counter_c = 0
        counter_n = 0
        counter_o = 0
        user_output = ""

