one_lev = int(input())
two_leva = int(input())
five_leva = int(input())
sum = int(input())

for i in range(one_lev + 1):
    for j in range(two_leva + 1):
        for k in range(five_leva + 1):
            if i + j * 2 + k * 5 == sum:
                print(f"{i} * 1 lv. + {j} * 2 lv. + {k} * 5 lv. = {sum} lv.")
