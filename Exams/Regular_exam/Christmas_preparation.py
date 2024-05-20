gift_paper = int(input())
fabric = int(input())
glue = float(input())
discount = int(input()) / 100

total = gift_paper * 5.8 + fabric * 7.2 + glue * 1.2

total -= total * discount

print(f"{total:.3f}")
