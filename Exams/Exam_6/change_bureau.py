bitcoin = int(input()) * 1168
chineese = float(input()) * 0.15 * 1.76
comision = float(input()) / 100

total = bitcoin + chineese
total /= 1.95

total -= total * comision
print(f"{total:.2f}")