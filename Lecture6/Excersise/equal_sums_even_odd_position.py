num1 = int(input())
num2 = int(input())

for i in range(num1, num2 + 1):
    sum_odd = 0
    sum_even = 0
    for index, el in (enumerate(str(i))):

        if index % 2 == 0:
            sum_odd += int(el)
        else:
            sum_even += int(el)

    if sum_even == sum_odd:
        print(f"{i}", end= " ")
