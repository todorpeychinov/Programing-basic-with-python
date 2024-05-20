company = input()
adults_tickets = int(input())
kids_tickets = int(input())
adults_price = float(input())
extra_tax = float(input())

kids_price = 0.3 * adults_price + extra_tax
adults_price += extra_tax



total = adults_price * adults_tickets + kids_price * kids_tickets

print(f"The profit of your agency from {company} tickets is {0.2 * total:.2f} lv.")