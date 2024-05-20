from math import sqrt

sum_prime = 0
sum_non_prime = 0

while True:

    num = input()

    if num == "stop":
        break

    num = int(num)

    if num < 0:
        print("Number is negative.")
        continue

    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            sum_non_prime += num
            break

    else:
        sum_prime += num

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")

