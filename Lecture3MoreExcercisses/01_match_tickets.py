budget = float(input())
category = input()
people_count = int(input())
output = ""
tickets_cost = 0

if people_count <= 4:
    budget -= budget * 0.75
elif 4 < people_count <= 9:
    budget -= budget * 0.60
elif 9 < people_count <= 24:
    budget -= budget * 0.5
elif 24 < people_count <= 49:
    budget -= budget * 0.4
elif budget >= 50 :
    budget -= budget * 0.25

if category == "VIP":
    tickets_cost = people_count * 499.99
else:
    tickets_cost = people_count * 249.99

if budget >= tickets_cost:
    print(f"Yes! You have {(budget - tickets_cost):.2f} leva left.")
else:
    print(f"Not enough money! You need {(tickets_cost - budget):.2f} leva.")