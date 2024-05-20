max_num1 = int(input())
max_num2 = int(input())
max_pass_num = int(input())
counter = 0
char_A = 35
char_B = 64

for i in range(1, max_num1 + 1):
    for j in range(1, max_num2 + 1):
        counter += 1
        print(f"{chr(char_A)}{chr(char_B)}{i}{j}{chr(char_B)}{chr(char_A)}|", end="")
        if counter >= max_pass_num:
            exit()
        char_A += 1
        char_B += 1
        if char_A > 55:
            char_A = 35
        if char_B > 96:
            char_B = 64

