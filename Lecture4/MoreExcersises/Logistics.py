

n = int(input())
percent_by_bus = 0.00
percent_by_truck = 0.00
percent_by_train = 0.00
weight_by_bus = 0
weight_by_truck = 0
weight_by_train = 0
total_weight = 0



for i in range(n):
    weight = int(input())
    total_weight += weight
    if weight <= 3:
        weight_by_bus += weight
    elif 4 <= weight <= 11:
        weight_by_truck += weight
    else:
        weight_by_train += weight

average = (weight_by_bus * 200 + weight_by_truck * 175 + weight_by_train * 120) / total_weight
average = round(average,2)
percent_by_bus = weight_by_bus / total_weight * 100
percent_by_truck = weight_by_truck / total_weight * 100
percent_by_train = weight_by_train / total_weight * 100

print(f"{average:.2f}")
print(f"{percent_by_bus:.2f}%")
print(f"{percent_by_truck:.2f}%")
print(f"{percent_by_train:.2f}%")

