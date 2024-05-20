user_input = input()
sum = 0

for i in range(len(user_input)):
    if user_input[i] == 'a':
        sum += 1
    elif user_input[i] == 'e':
        sum += 2
    elif user_input[i] == 'i':
        sum += 3
    elif user_input[i] == 'o':
        sum += 4
    elif user_input[i] == 'u':
        sum += 5

print(sum)
